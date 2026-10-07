<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'meter',
  endpoint: '/api/meter',
  label: '关口表计',
  title: '关口计量管理',
  desc: '维护关口表计，围绕表计编号、计量点名称、表计精度、正向有功电量做登记、筛选与状态流转。',
  keywordLabel: '表计编号',
  columns: ['表计编号', '计量点名称', '表计精度', '正向有功电量', '反向有功电量', '上月示数', '本月示数', '通讯状态'],
  actions: ['确认正常', '标记异常', '停用表计'],
  statuses: ['通讯正常', '数据异常', '通讯中断', '已停用'],
  stats: [{ label: "日发电量", value: 0 }, { label: "日上网电量", value: 0 }, { label: "异常表计数", value: 0 }],
}
</script>
