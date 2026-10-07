<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'safety',
  endpoint: '/api/safety',
  label: '安全措施票',
  title: '安全措施管理',
  desc: '维护安全措施票，围绕措施编号、措施类型、涉及设备、签发人做登记、筛选与状态流转。',
  keywordLabel: '措施编号',
  columns: ['措施编号', '措施类型', '涉及设备', '签发人', '执行人', '监护人', '有效期至', '措施状态'],
  actions: ['签发措施', '开始执行', '解除措施'],
  statuses: ['待签发', '已签发', '执行中', '已解除'],
  stats: [{ label: "待签发票", value: 0 }, { label: "执行中票", value: 0 }, { label: "今日解除数", value: 0 }],
}
</script>
