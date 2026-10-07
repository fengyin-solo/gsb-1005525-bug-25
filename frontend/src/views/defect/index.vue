<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'defect',
  endpoint: '/api/defect',
  label: '设备缺陷',
  title: '缺陷管理管理',
  desc: '维护设备缺陷，围绕缺陷编号、发现日期、缺陷设备、缺陷类别做登记、筛选与状态流转。',
  keywordLabel: '缺陷编号',
  columns: ['缺陷编号', '发现日期', '缺陷设备', '缺陷类别', '严重等级', '处理方案', '整改时限', '缺陷状态'],
  actions: ['分派处理', '提交验收', '关闭缺陷'],
  statuses: ['待分派', '处理中', '已验收', '已关闭'],
  stats: [{ label: "待处理缺陷", value: 0 }, { label: "处理中缺陷", value: 0 }, { label: "超期缺陷", value: 0 }],
}
</script>
