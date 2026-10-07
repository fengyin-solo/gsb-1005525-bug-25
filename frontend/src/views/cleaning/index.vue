<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'cleaning',
  endpoint: '/api/cleaning',
  label: '清洗任务',
  title: '组件清洗管理',
  desc: '维护清洗任务，围绕任务编号、清洗区域、清洗方式、计划日期做登记、筛选与状态流转。',
  keywordLabel: '任务编号',
  columns: ['任务编号', '清洗区域', '清洗方式', '计划日期', '作业人员', '用水吨数', '清洗后PR值', '清洗状态'],
  actions: ['排期确认', '开始作业', '验收完成'],
  statuses: ['待排期', '已排期', '作业中', '已完成'],
  stats: [{ label: "待清洗片区", value: 0 }, { label: "今日作业量", value: 0 }, { label: "本月清洗面积", value: 0 }],
}
</script>
