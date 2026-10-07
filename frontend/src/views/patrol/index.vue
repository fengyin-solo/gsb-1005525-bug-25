<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'patrol',
  endpoint: '/api/patrol',
  label: '巡视记录',
  title: '巡视检查管理',
  desc: '维护巡视记录，围绕记录编号、巡视区域、巡视日期、巡视人员做登记、筛选与状态流转。',
  keywordLabel: '记录编号',
  columns: ['记录编号', '巡视区域', '巡视日期', '巡视人员', '发现缺陷数', '红外测温结果', '接线端子温度', '巡视状态'],
  actions: ['开始巡视', '提交记录', '归档记录'],
  statuses: ['待巡视', '巡视中', '已记录', '已归档'],
  stats: [{ label: "今日巡视数", value: 0 }, { label: "发现缺陷数", value: 0 }, { label: "待巡视区域", value: 0 }],
}
</script>
