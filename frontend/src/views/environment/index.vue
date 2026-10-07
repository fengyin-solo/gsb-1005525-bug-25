<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'environment',
  title: "环境监测站管理",
  description: "维护环境监测站，围绕站点编号、安装位置、辐照度、环境温度做登记、筛选与状态流转。",
  entityLabel: "环境监测站",
  exportLabel: "环境监测站清单",
  emptyText: "暂无环境监测站数据，可先登记环境监测站",
  columns: ["站点编号","安装位置","辐照度","环境温度","风速","风向","积灰比","通讯状态"],
  filterFields: ["站点编号","安装位置","辐照度"],
  statuses: ["数据正常","数据异常","传感器故障","已停用"],
  actions: ["恢复正常","标记异常","停用站点"],
  stats: [{"label":"当日辐照总量","value":0},{"label":"环境平均温度","value":0},{"label":"故障站点数","value":0}],
}
</script>
