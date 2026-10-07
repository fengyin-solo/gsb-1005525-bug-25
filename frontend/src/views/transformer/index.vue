<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'transformer',
  title: "变压器监视管理",
  description: "维护变压器，围绕变压器编号、电压等级、额定容量、油温上限做登记、筛选与状态流转。",
  entityLabel: "变压器",
  exportLabel: "变压器监视清单",
  emptyText: "暂无变压器监视数据，可先登记变压器",
  columns: ["变压器编号","电压等级","额定容量","油温上限","绕组温度","油位状态","瓦斯保护状态","运行状态"],
  filterFields: ["变压器编号","电压等级","额定容量"],
  statuses: ["正常运行","过负荷","油温异常","待检修"],
  actions: ["恢复正常","降负荷运行","安排检修"],
  stats: [{"label":"运行变压器","value":0},{"label":"超温台数","value":0},{"label":"待检台数","value":0}],
}
</script>
