<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'maintenance',
  title: "检修计划管理",
  description: "维护检修计划，围绕计划编号、检修设备、检修类别、计划开始做登记、筛选与状态流转。",
  entityLabel: "检修计划",
  exportLabel: "检修计划清单",
  emptyText: "暂无检修计划数据，可先登记检修计划",
  columns: ["计划编号","检修设备","检修类别","计划开始","计划结束","责任人","安全措施","计划状态"],
  filterFields: ["计划编号","检修设备","检修类别"],
  statuses: ["待审批","已批复","执行中","已完工"],
  actions: ["提交审批","开始执行","确认完工"],
  stats: [{"label":"待审批计划","value":0},{"label":"执行中计划","value":0},{"label":"本月完工数","value":0}],
}
</script>
