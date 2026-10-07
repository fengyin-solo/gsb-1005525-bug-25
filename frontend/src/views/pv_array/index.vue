<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'pv_array',
  endpoint: '/api/pv_array',
  label: '光伏阵列',
  title: '光伏阵列管理',
  desc: '维护光伏阵列，围绕阵列编号、所属片区、组件型号、单块功率做登记、筛选与状态流转。',
  keywordLabel: '阵列编号',
  columns: ['阵列编号', '所属片区', '组件型号', '单块功率', '串联片数', '总装机容量', '投运日期', '阵列状态'],
  actions: ['恢复全功率', '降功率运行', '申请停机'],
  statuses: ['运行中', '限功率', '计划停机', '故障停机'],
  stats: [{ label: "运行阵列数", value: 0 }, { label: "限电阵列数", value: 0 }, { label: "故障停机数", value: 0 }],
}
</script>
