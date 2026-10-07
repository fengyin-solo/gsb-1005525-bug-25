<template>
  <ListPage :config="config" />
</template>

<script setup lang="ts">
import ListPage from '@/components/ListPage.vue'
import type { ListPageConfig } from '@/composables/useListPage'

const config: ListPageConfig = {
  module: 'energy_storage',
  endpoint: '/api/energy_storage',
  label: '储能电池组',
  title: '储能电池组管理',
  desc: '维护储能电池组，围绕电池组编号、电池类型、额定容量、SOC上限做登记、筛选与状态流转。',
  keywordLabel: '电池组编号',
  columns: ['电池组编号', '电池类型', '额定容量', 'SOC上限', '充放电循环', '电池温度', '内阻变化率', '运行状态'],
  actions: ['启动充电', '启动放电', '切换到待机'],
  statuses: ['充电中', '放电中', '待机', '故障停机'],
  stats: [{ label: "SOC均值", value: 0 }, { label: "充放电组数", value: 0 }, { label: "故障组数", value: 0 }],
}
</script>
