<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'combiner_box',
  endpoint: '/api/combiner_box',
  label: '汇流箱',
  title: '汇流箱检测管理',
  desc: '维护汇流箱，围绕汇流箱编号、所属阵列、输入路数、熔断器状态做登记、筛选与状态流转。',
  keywordLabel: '汇流箱编号',
  columns: ['汇流箱编号', '所属阵列', '输入路数', '熔断器状态', '防雷模块状态', '通讯状态', '箱体温度', '运行状态'],
  actions: ['恢复正常', '标记异常', '停用设备'],
  statuses: ['运行正常', '熔断器异常', '通讯中断', '已停用'],
  stats: [{ label: "正常运行数", value: 0 }, { label: "异常汇流箱", value: 0 }, { label: "停用设备数", value: 0 }],
}
</script>
