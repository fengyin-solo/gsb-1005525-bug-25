<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'environment',
  endpoint: '/api/environment',
  label: '环境监测站',
  title: '环境监测站管理',
  desc: '维护环境监测站，围绕站点编号、安装位置、辐照度、环境温度做登记、筛选与状态流转。',
  keywordLabel: '站点编号',
  columns: ['站点编号', '安装位置', '辐照度', '环境温度', '风速', '风向', '积灰比', '通讯状态'],
  actions: ['恢复正常', '标记异常', '停用站点'],
  statuses: ['数据正常', '数据异常', '传感器故障', '已停用'],
  stats: [{ label: "当日辐照总量", value: 0 }, { label: "环境平均温度", value: 0 }, { label: "故障站点数", value: 0 }],
}
</script>
