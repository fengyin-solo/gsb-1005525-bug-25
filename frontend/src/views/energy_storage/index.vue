<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'energy_storage',
  title: "储能电池组管理",
  description: "维护储能电池组，围绕电池组编号、电池类型、额定容量、SOC上限做登记、筛选与状态流转。",
  entityLabel: "储能电池组",
  exportLabel: "储能电池组清单",
  emptyText: "暂无储能电池组数据，可先登记储能电池组",
  columns: ["电池组编号","电池类型","额定容量","SOC上限","充放电循环","电池温度","内阻变化率","运行状态"],
  filterFields: ["电池组编号","电池类型","额定容量"],
  statuses: ["充电中","放电中","待机","故障停机"],
  actions: ["启动充电","启动放电","切换到待机"],
  stats: [{"label":"SOC均值","value":0},{"label":"充放电组数","value":0},{"label":"故障组数","value":0}],
}
</script>
