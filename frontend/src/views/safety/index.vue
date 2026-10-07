<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'safety',
  title: "安全措施管理",
  description: "维护安全措施票，围绕措施编号、措施类型、涉及设备、签发人做登记、筛选与状态流转。",
  entityLabel: "安全措施票",
  exportLabel: "安全措施清单",
  emptyText: "暂无安全措施数据，可先登记安全措施票",
  columns: ["措施编号","措施类型","涉及设备","签发人","执行人","监护人","有效期至","措施状态"],
  filterFields: ["措施编号","措施类型","涉及设备"],
  statuses: ["待签发","已签发","执行中","已解除"],
  actions: ["签发措施","开始执行","解除措施"],
  stats: [{"label":"待签发票","value":0},{"label":"执行中票","value":0},{"label":"今日解除数","value":0}],
}
</script>
