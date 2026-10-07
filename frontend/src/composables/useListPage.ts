import { computed, onMounted, ref } from 'vue'

import { request } from '@/api/client'
import { useListCacheStore, type Row } from '@/stores/listCache'

/** 列表页配置：18 个业务模块共用一套列表行为，差异只在这份配置里。 */
export interface ListPageConfig {
  module: string
  endpoint: string
  label: string
  title: string
  desc: string
  keywordLabel: string
  columns: string[]
  actions: string[]
  statuses: string[]
  stats: { label: string; value: number }[]
}

/**
 * 列表页统一状态机：筛选、排序、分页、导出只走这一套。
 *
 * 口径约定（与后端 app.listing 对齐）：
 * - 页码、每页条数、总数以接口返回为准，前端不自己另算一套；
 * - 非法页码由后端回到第一页并在 notice 写明原因，前端跟随返回的 page；
 * - 筛选条件或翻页顺序变化时先清掉旧数据再拉取，缓存不残留；
 * - 每次拉取成功后把完整状态存入快照，返回/刷新时与最后一次拉取一致。
 */
export function useListPage(config: ListPageConfig) {
  const cache = useListCacheStore()
  const snapshot = cache.snapshots[config.module]

  const keyword = ref(snapshot?.keyword ?? '')
  const status = ref(snapshot?.status ?? '')
  const order = ref<'asc' | 'desc'>(snapshot?.order ?? 'desc')
  const page = ref(snapshot?.page ?? 1)
  const size = ref(snapshot?.size ?? 20)
  const total = ref(snapshot?.total ?? 0)
  const rows = ref<Row[]>(snapshot?.rows ?? [])
  const notice = ref('')
  const errorMessage = ref('')
  const loading = ref(false)

  const maxPage = computed(() => Math.max(1, Math.ceil(total.value / size.value)))

  function filterParams(): URLSearchParams {
    const params = new URLSearchParams()
    const kw = keyword.value.trim()
    if (kw) params.set('keyword', kw)
    if (status.value) params.set('status', status.value)
    params.set('order', order.value)
    return params
  }

  /** 条件变化后、重新拉取前：上一次的列表数据不能残留在页面上。 */
  function invalidate() {
    rows.value = []
    total.value = 0
    notice.value = ''
  }

  async function fetchPage() {
    loading.value = true
    errorMessage.value = ''
    try {
      const params = filterParams()
      params.set('page', String(page.value))
      params.set('size', String(size.value))
      const response = await request(`${config.endpoint}?${params.toString()}`)
      if (!response.ok) {
        throw new Error(`${config.label}列表读取失败`)
      }
      const payload = await response.json()
      rows.value = payload.items ?? []
      total.value = payload.total ?? 0
      page.value = payload.page ?? 1
      size.value = payload.size ?? size.value
      notice.value = payload.notice ?? ''
      cache.save(config.module, {
        keyword: keyword.value,
        status: status.value,
        order: order.value,
        page: page.value,
        size: size.value,
        total: total.value,
        rows: rows.value,
      })
    } catch (error) {
      errorMessage.value = error instanceof Error ? error.message : `${config.label}列表读取失败`
    } finally {
      loading.value = false
    }
  }

  function applyFilters() {
    page.value = 1
    invalidate()
    void fetchPage()
  }

  function resetFilters() {
    keyword.value = ''
    status.value = ''
    page.value = 1
    invalidate()
    void fetchPage()
  }

  function changePage(next: number) {
    if (next === page.value) return
    page.value = next
    invalidate()
    void fetchPage()
  }

  function changeSize(next: number) {
    if (next === size.value) return
    size.value = next
    page.value = 1
    invalidate()
    void fetchPage()
  }

  function toggleOrder() {
    order.value = order.value === 'desc' ? 'asc' : 'desc'
    page.value = 1
    invalidate()
    void fetchPage()
  }

  /** 导出按当前筛选条件取全量：条数与列表总数同一份口径，结果落库。 */
  async function exportRows() {
    errorMessage.value = ''
    try {
      const params = filterParams()
      const response = await request(`${config.endpoint}/export?${params.toString()}`)
      if (!response.ok) {
        throw new Error(`${config.label}导出失败`)
      }
      const payload = await response.json()
      const consistency = payload.total === total.value
        ? '与列表总数一致'
        : `列表当前总数 ${total.value} 条，以导出时刻数据为准`
      notice.value = `已按当前条件导出 ${payload.total} 条（${consistency}），落库记录 #${payload.record.id}`
    } catch (error) {
      errorMessage.value = error instanceof Error ? error.message : `${config.label}导出失败`
    }
  }

  async function runAction(action: string, row: Row) {
    errorMessage.value = ''
    try {
      const response = await request(`${config.endpoint}/${row.id}/actions`, {
        method: 'POST',
        body: JSON.stringify({ values: { action } }),
      })
      if (!response.ok) {
        throw new Error(`${config.label}动作未生效，请稍后重试`)
      }
      const result = await response.json()
      if (!result.ok) {
        throw new Error(result.message || `${config.label}动作未生效`)
      }
      notice.value = result.message ?? ''
      await fetchPage()
    } catch (error) {
      errorMessage.value = error instanceof Error ? error.message : `${config.label}操作失败`
    }
  }

  onMounted(fetchPage)

  return {
    keyword,
    status,
    order,
    page,
    size,
    total,
    rows,
    notice,
    errorMessage,
    loading,
    maxPage,
    applyFilters,
    resetFilters,
    changePage,
    changeSize,
    toggleOrder,
    exportRows,
    runAction,
  }
}
