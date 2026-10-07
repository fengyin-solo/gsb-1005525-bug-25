<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'contract',
  title: "运维合同管理",
  description: "维护运维合同，围绕合同编号、合同名称、签约甲方、签约乙方做登记、筛选与状态流转。",
  entityLabel: "运维合同",
  exportLabel: "运维合同清单",
  emptyText: "暂无运维合同数据，可先登记运维合同",
  columns: ["合同编号","合同名称","签约甲方","签约乙方","合同金额","起止日期","续签条款","合同状态"],
  filterFields: ["合同编号","合同名称","签约甲方"],
  statuses: ["草稿中","已签订","履行中","已到期","已终止"],
  actions: ["确认签订","开始履行","终止合同"],
  stats: [{"label":"履行中合同","value":0},{"label":"本月到期合同","value":0},{"label":"待签订合同","value":0}],
}
</script>
