<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'boosting_station',
  endpoint: '/api/boosting_station',
  label: '升压站',
  title: '升压站监视管理',
  desc: '维护升压站，围绕升压站编号、进线电压、出线电压、主变容量做登记、筛选与状态流转。',
  keywordLabel: '升压站编号',
  columns: ['升压站编号', '进线电压', '出线电压', '主变容量', '母线状态', '断路器状态', '无功补偿', '运行状态'],
  actions: ['恢复正常', '检查保护', '安排检修'],
  statuses: ['正常运行', '非全相运行', '保护动作', '待检修'],
  stats: [{ label: "并网电压", value: 0 }, { label: "无功出力", value: 0 }, { label: "保护动作次数", value: 0 }],
}
</script>
