<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage, { type ModuleConfig } from '@/components/ListPage.vue'

const config: ModuleConfig = {
  module: 'cleaning',
  title: "组件清洗管理",
  description: "维护清洗任务，围绕任务编号、清洗区域、清洗方式、计划日期做登记、筛选与状态流转。",
  entityLabel: "清洗任务",
  exportLabel: "组件清洗清单",
  emptyText: "暂无组件清洗数据，可先登记清洗任务",
  columns: ["任务编号","清洗区域","清洗方式","计划日期","作业人员","用水吨数","清洗后PR值","清洗状态"],
  filterFields: ["任务编号","清洗区域","清洗方式"],
  statuses: ["待排期","已排期","作业中","已完成"],
  actions: ["排期确认","开始作业","验收完成"],
  stats: [{"label":"待清洗片区","value":0},{"label":"今日作业量","value":0},{"label":"本月清洗面积","value":0}],
}
</script>
