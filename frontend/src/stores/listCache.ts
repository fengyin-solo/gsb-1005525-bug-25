import { defineStore } from 'pinia'

export type Row = Record<string, string | number | null>

/** 一个模块列表最后一次成功拉取时的完整状态。 */
export interface ListSnapshot {
  keyword: string
  status: string
  order: 'asc' | 'desc'
  page: number
  size: number
  total: number
  rows: Row[]
}

/**
 * 各模块列表的最后一次拉取快照。
 * 返回或刷新页面时据此恢复，保证页码与总数和最后一次拉取一致；
 * 每次拉取成功后整体覆盖，筛选或排序变化时由调用方先清掉旧数据，
 * 上一次的缓存不会残留在页面上。
 */
export const useListCacheStore = defineStore('listCache', {
  state: () => ({
    snapshots: {} as Record<string, ListSnapshot>,
  }),
  actions: {
    save(module: string, snapshot: ListSnapshot) {
      this.snapshots[module] = snapshot
    },
  },
})
