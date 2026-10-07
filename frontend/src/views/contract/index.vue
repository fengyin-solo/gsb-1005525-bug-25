<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'contract',
  endpoint: '/api/contract',
  label: '运维合同',
  title: '运维合同管理',
  desc: '维护运维合同，围绕合同编号、合同名称、签约甲方、签约乙方做登记、筛选与状态流转。',
  keywordLabel: '合同编号',
  columns: ['合同编号', '合同名称', '签约甲方', '签约乙方', '合同金额', '起止日期', '续签条款', '合同状态'],
  actions: ['确认签订', '开始履行', '终止合同'],
  statuses: ['草稿中', '已签订', '履行中', '已到期', '已终止'],
  stats: [{ label: "履行中合同", value: 0 }, { label: "本月到期合同", value: 0 }, { label: "待签订合同", value: 0 }],
}
</script>
