<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'dispatch',
  endpoint: '/api/dispatch',
  label: '调度指令单',
  title: '调度指令管理',
  desc: '维护调度指令单，围绕指令编号、下发单位、指令类型、下发时间做登记、筛选与状态流转。',
  keywordLabel: '指令编号',
  columns: ['指令编号', '下发单位', '指令类型', '下发时间', '执行时限', '执行人', '执行结果', '指令状态'],
  actions: ['确认执行', '完成回复', '驳回指令'],
  statuses: ['待执行', '执行中', '已完成', '已驳回'],
  stats: [{ label: "待执行指令", value: 0 }, { label: "今日完成数", value: 0 }, { label: "驳回指令数", value: 0 }],
}
</script>
