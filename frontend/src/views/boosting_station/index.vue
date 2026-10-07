<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'boosting_station',
  title: "升压站监视管理",
  description: "维护升压站，围绕升压站编号、进线电压、出线电压、主变容量做登记、筛选与状态流转。",
  entityLabel: "升压站",
  exportLabel: "升压站监视清单",
  emptyText: "暂无升压站监视数据，可先登记升压站",
  columns: ["升压站编号","进线电压","出线电压","主变容量","母线状态","断路器状态","无功补偿","运行状态"],
  filterFields: ["升压站编号","进线电压","出线电压"],
  statuses: ["正常运行","非全相运行","保护动作","待检修"],
  actions: ["恢复正常","检查保护","安排检修"],
  stats: [{"label":"并网电压","value":0},{"label":"无功出力","value":0},{"label":"保护动作次数","value":0}],
}
</script>
