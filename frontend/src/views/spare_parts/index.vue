<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'spare_parts',
  title: "备品备件管理",
  description: "维护备件物料，围绕备件编号、备件名称、规格型号、适用设备做登记、筛选与状态流转。",
  entityLabel: "备件物料",
  exportLabel: "备品备件清单",
  emptyText: "暂无备品备件数据，可先登记备件物料",
  columns: ["备件编号","备件名称","规格型号","适用设备","安全存量","当前存量","存放位置","备件状态"],
  filterFields: ["备件编号","备件名称","规格型号"],
  statuses: ["存量充足","低于安全量","已用尽","已废弃"],
  actions: ["入库登记","领用出库","标记废弃"],
  stats: [{"label":"备件种类数","value":0},{"label":"低存量备件","value":0},{"label":"本月领用数","value":0}],
}
</script>
