<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'transformer',
  endpoint: '/api/transformer',
  label: '变压器',
  title: '变压器监视管理',
  desc: '维护变压器，围绕变压器编号、电压等级、额定容量、油温上限做登记、筛选与状态流转。',
  keywordLabel: '变压器编号',
  columns: ['变压器编号', '电压等级', '额定容量', '油温上限', '绕组温度', '油位状态', '瓦斯保护状态', '运行状态'],
  actions: ['恢复正常', '降负荷运行', '安排检修'],
  statuses: ['正常运行', '过负荷', '油温异常', '待检修'],
  stats: [{ label: "运行变压器", value: 0 }, { label: "超温台数", value: 0 }, { label: "待检台数", value: 0 }],
}
</script>
