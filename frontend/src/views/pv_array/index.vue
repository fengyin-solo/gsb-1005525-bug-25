<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'pv_array',
  title: "光伏阵列管理",
  description: "维护光伏阵列，围绕阵列编号、所属片区、组件型号、单块功率做登记、筛选与状态流转。",
  entityLabel: "光伏阵列",
  exportLabel: "光伏阵列清单",
  emptyText: "暂无光伏阵列数据，可先登记光伏阵列",
  columns: ["阵列编号","所属片区","组件型号","单块功率","串联片数","总装机容量","投运日期","阵列状态"],
  filterFields: ["阵列编号","所属片区","组件型号"],
  statuses: ["运行中","限功率","计划停机","故障停机"],
  actions: ["恢复全功率","降功率运行","申请停机"],
  stats: [{"label":"运行阵列数","value":0},{"label":"限电阵列数","value":0},{"label":"故障停机数","value":0}],
}
</script>
