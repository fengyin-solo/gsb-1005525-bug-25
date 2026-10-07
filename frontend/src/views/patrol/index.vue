<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'patrol',
  title: "巡视检查管理",
  description: "维护巡视记录，围绕记录编号、巡视区域、巡视日期、巡视人员做登记、筛选与状态流转。",
  entityLabel: "巡视记录",
  exportLabel: "巡视检查清单",
  emptyText: "暂无巡视检查数据，可先登记巡视记录",
  columns: ["记录编号","巡视区域","巡视日期","巡视人员","发现缺陷数","红外测温结果","接线端子温度","巡视状态"],
  filterFields: ["记录编号","巡视区域","巡视日期"],
  statuses: ["待巡视","巡视中","已记录","已归档"],
  actions: ["开始巡视","提交记录","归档记录"],
  stats: [{"label":"今日巡视数","value":0},{"label":"发现缺陷数","value":0},{"label":"待巡视区域","value":0}],
}
</script>
