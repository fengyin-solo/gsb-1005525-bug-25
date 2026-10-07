<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'report',
  title: "运行月报管理",
  description: "维护运行月报，围绕月报编号、统计月份、发电量、等效利用小时做登记、筛选与状态流转。",
  entityLabel: "运行月报",
  exportLabel: "运行月报清单",
  emptyText: "暂无运行月报数据，可先登记运行月报",
  columns: ["月报编号","统计月份","发电量","等效利用小时","综合效率PR","设备可利用率","故障停机时间","月报状态"],
  filterFields: ["月报编号","统计月份","发电量"],
  statuses: ["待填写","已填写","已审核","已发布"],
  actions: ["填写月报","提交审核","发布月报"],
  stats: [{"label":"当月发电量","value":0},{"label":"当月PR值","value":0},{"label":"待填月报数","value":0}],
}
</script>
