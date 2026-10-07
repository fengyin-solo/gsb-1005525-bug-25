<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'inverter',
  title: "逆变器监视管理",
  description: "维护逆变器，围绕逆变器编号、品牌型号、额定功率、输入电压范围做登记、筛选与状态流转。",
  entityLabel: "逆变器",
  exportLabel: "逆变器监视清单",
  emptyText: "暂无逆变器监视数据，可先登记逆变器",
  columns: ["逆变器编号","品牌型号","额定功率","输入电压范围","所属阵列","运行温度","日均发电量","运行状态"],
  filterFields: ["逆变器编号","品牌型号","额定功率"],
  statuses: ["正常运行","降容运行","高温报警","待检修"],
  actions: ["恢复运行","降容保护","安排检修"],
  stats: [{"label":"在线逆变器","value":0},{"label":"降容台数","value":0},{"label":"报修台数","value":0}],
}
</script>
