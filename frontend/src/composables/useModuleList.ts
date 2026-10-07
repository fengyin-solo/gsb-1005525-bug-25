/**
 * 列表分页/筛选/导出的唯一口径。
 *
 * 规则：
 * - page/size/total 一律以接口返回为准（响应里的 page/size/total 覆盖本地状态），
 *   本地只负责发起请求；冲突或非法页码由服务端校正，原因在 notice 里展示。
 * - 缓存只保存“最后一次成功拉取”的状态与结果（按模块独立的 sessionStorage 键）；
 *   筛选条件、翻页、每页条数的任何变化都先作废当前状态再请求，不残留上一次内容。
 * - 刷新或返回本页时，用缓存的条件直接拉取并对账，页面与总数和上次离开时一致。
 * - 导出与列表发同一份条件，导出条数即列表 total。
 */
import { ref } from 'vue'

import { request } from '@/api/client'

export interface ListPayload {
  items: Record<string, string | number | null>[]
  total: number
  page: number
  size: number
  notice?: string
}

export interface ListConfig {
  /** 模块接口前缀，例如 /api/pv_array */
  endpoint: string
  /** sessionStorage 隔离键，通常与模块名一致 */
  cacheKey: string
}

interface CacheShape {
  page: number
  size: number
  total: number
  keyword: string
  status: string
  filters: Record<string, string>
  items: ListPayload['items']
}

export function useModuleList(config: ListConfig) {
  const storageKey = `module-list:${config.cacheKey}`

  const rows = ref<ListPayload['items']>([])
  const total = ref(0)
  const page = ref(1)
  const size = ref(20)
  const keyword = ref('')
  const status = ref('')
  const filters = ref<Record<string, string>>({})
  const notice = ref('')
  const errorMessage = ref('')
  const loading = ref(false)

  let requestSeq = 0

  function body(): Record<string, unknown> {
    return {
      keyword: keyword.value || null,
      status: status.value || null,
      filters: filters.value,
      page: page.value,
      size: size.value,
      // 回传缓存总数，服务端对账冲突时以接口返回为准
      total: total.value,
    }
  }

  function persistCache() {
    const snapshot: CacheShape = {
      page: page.value,
      size: size.value,
      total: total.value,
      keyword: keyword.value,
      status: status.value,
      filters: { ...filters.value },
      items: rows.value,
    }
    sessionStorage.setItem(storageKey, JSON.stringify(snapshot))
  }

  /** 按当前状态拉取；只有最新一次请求能落状态，避免乱序残留。 */
  async function fetchList(keepStale: boolean): Promise<void> {
    const seq = ++requestSeq
    loading.value = true
    errorMessage.value = ''
    try {
      const response = await request(`${config.endpoint}/list`, {
        method: 'POST',
        body: JSON.stringify(body()),
      })
      if (!response.ok) {
        throw new Error('列表读取失败')
      }
      const payload = (await response.json()) as ListPayload
      if (seq !== requestSeq) {
        return // 已有更新的条件/翻页请求发出，本次结果作废，不能覆盖新状态
      }
      applyPayload(payload)
      persistCache()
    } catch (error) {
      if (seq !== requestSeq) {
        return
      }
      if (!keepStale) {
        // 条件已变化，旧缓存不能继续展示，宁可清空
        rows.value = []
        total.value = 0
      }
      errorMessage.value = error instanceof Error ? error.message : '列表读取失败'
    } finally {
      if (seq === requestSeq) {
        loading.value = false
      }
    }
  }

  function applyPayload(payload: ListPayload) {
    // 权威状态：页码、每页条数、总数全部以接口返回为准
    rows.value = payload.items ?? []
    total.value = payload.total ?? rows.value.length
    page.value = payload.page
    size.value = payload.size
    notice.value = payload.notice ?? ''
  }

  /** 条件/翻页变化：先作废旧内容再拉，避免上一次筛选的行或总数残留。 */
  function invalidateAndFetch(): void {
    requestSeq += 1
    rows.value = []
    total.value = 0
    notice.value = ''
    void fetchList(false)
  }

  function applySearch(next: { keyword?: string; status?: string; filters?: Record<string, string> }): void {
    keyword.value = next.keyword ?? ''
    status.value = next.status ?? ''
    filters.value = next.filters ? { ...next.filters } : {}
    page.value = 1
    invalidateAndFetch()
  }

  function search(): void {
    page.value = 1
    invalidateAndFetch()
  }

  function resetFilters(): void {
    applySearch({ keyword: '', status: '', filters: {} })
  }

  function gotoPage(nextPage: number): void {
    if (nextPage === page.value) {
      return
    }
    page.value = nextPage
    invalidateAndFetch()
  }

  function changeSize(nextSize: number): void {
    if (nextSize === size.value) {
      return
    }
    size.value = nextSize
    page.value = 1
    invalidateAndFetch()
  }

  /** 进入页面：有缓存就按“最后一次成功拉取”的条件恢复并对账，无缓存才用初始条件。 */
  function restoreOrInit(): void {
    const raw = sessionStorage.getItem(storageKey)
    if (raw) {
      try {
        const cached = JSON.parse(raw) as CacheShape
        page.value = cached.page
        size.value = cached.size
        total.value = cached.total
        keyword.value = cached.keyword
        status.value = cached.status
        filters.value = cached.filters
        // 先还原上次内容避免闪烁；请求成功后由接口权威结果覆盖，失败则保留
        rows.value = cached.items
      } catch {
        sessionStorage.removeItem(storageKey)
      }
    }
    void fetchList(true)
  }

  /** 导出当前条件下的全量数据，并触发 JSON 文件下载。 */
  async function exportRows(): Promise<void> {
    errorMessage.value = ''
    notice.value = ''
    try {
      const response = await request(`${config.endpoint}/export`, {
        method: 'POST',
        body: JSON.stringify(body()),
      })
      if (!response.ok) {
        throw new Error('导出失败')
      }
      const payload = (await response.json()) as ListPayload & {
        module: string
        export_id: number
        created_at: string
      }
      // 导出条数与列表总数同源：总数仍以接口口径覆盖本地
      total.value = payload.total
      notice.value = `已按当前条件导出 ${payload.total} 条（导出记录 #${payload.export_id}，已落库）`
      const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' })
      const url = URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.href = url
      link.download = `${config.cacheKey}_export_${payload.export_id}.json`
      link.click()
      URL.revokeObjectURL(url)
    } catch (error) {
      errorMessage.value = error instanceof Error ? error.message : '导出失败'
    }
  }

  return {
    rows,
    total,
    page,
    size,
    keyword,
    status,
    filters,
    notice,
    errorMessage,
    loading,
    search,
    resetFilters,
    gotoPage,
    changeSize,
    applySearch,
    restoreOrInit,
    exportRows,
    refresh: () => { void fetchList(true) },
  }
}
