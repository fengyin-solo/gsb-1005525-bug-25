<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'spare_parts',
  endpoint: '/api/spare_parts',
  label: '备件物料',
  title: '备品备件管理',
  desc: '维护备件物料，围绕备件编号、备件名称、规格型号、适用设备做登记、筛选与状态流转。',
  keywordLabel: '备件编号',
  columns: ['备件编号', '备件名称', '规格型号', '适用设备', '安全存量', '当前存量', '存放位置', '备件状态'],
  actions: ['入库登记', '领用出库', '标记废弃'],
  statuses: ['存量充足', '低于安全量', '已用尽', '已废弃'],
  stats: [{ label: "备件种类数", value: 0 }, { label: "低存量备件", value: 0 }, { label: "本月领用数", value: 0 }],
}
</script>
