<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'meter',
  title: "关口计量管理",
  description: "维护关口表计，围绕表计编号、计量点名称、表计精度、正向有功电量做登记、筛选与状态流转。",
  entityLabel: "关口表计",
  exportLabel: "关口计量清单",
  emptyText: "暂无关口计量数据，可先登记关口表计",
  columns: ["表计编号","计量点名称","表计精度","正向有功电量","反向有功电量","上月示数","本月示数","通讯状态"],
  filterFields: ["表计编号","计量点名称","表计精度"],
  statuses: ["通讯正常","数据异常","通讯中断","已停用"],
  actions: ["确认正常","标记异常","停用表计"],
  stats: [{"label":"日发电量","value":0},{"label":"日上网电量","value":0},{"label":"异常表计数","value":0}],
}
</script>
