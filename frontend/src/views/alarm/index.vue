<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'alarm',
  title: "告警事件管理",
  description: "维护告警事件，围绕告警编号、告警来源、告警类型、触发时间做登记、筛选与状态流转。",
  entityLabel: "告警事件",
  exportLabel: "告警事件清单",
  emptyText: "暂无告警事件数据，可先登记告警事件",
  columns: ["告警编号","告警来源","告警类型","触发时间","告警阈值","当前值","确认人","告警状态"],
  filterFields: ["告警编号","告警来源","告警类型"],
  statuses: ["未确认","已确认","处理中","已消除"],
  actions: ["确认告警","开始处理","消除告警"],
  stats: [{"label":"未确认告警","value":0},{"label":"今日新增告警","value":0},{"label":"未消除告警","value":0}],
}
</script>
