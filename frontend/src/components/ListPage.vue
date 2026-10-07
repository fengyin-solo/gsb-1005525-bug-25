<template>
  <section class="page" :data-module="config.module">
    <header class="page-head">
      <div>
        <h2>{{ config.title }}</h2>
        <p class="page-desc">{{ config.description }}</p>
      </div>
      <div class="page-actions">
        <button class="btn primary" type="button" @click="openCreate">登记{{ config.entityLabel }}</button>
        <button class="btn" type="button" @click="exportRows">导出{{ config.exportLabel }}</button>
      </div>
    </header>

    <div class="stat-row">
      <article v-for="item in config.stats" :key="item.label" class="stat-card">
        <span class="stat-label">{{ item.label }}</span>
        <strong class="stat-value">{{ item.value }}</strong>
      </article>
    </div>

    <form class="filter-bar" @submit.prevent="onSearch">
      <label class="filter-item">
        <span>关键词</span>
        <input v-model="keywordModel" placeholder="按编号/名称检索" />
      </label>
      <label class="filter-item">
        <span>状态</span>
        <select v-model="statusModel">
          <option value="">全部状态</option>
          <option v-for="s in config.statuses" :key="s" :value="s">{{ s }}</option>
        </select>
      </label>
      <label v-for="field in config.filterFields" :key="field" class="filter-item">
        <span>{{ field }}</span>
        <input v-model="filtersModel[field]" :placeholder="`按${field}检索`" />
      </label>
      <button class="btn" type="submit">查询</button>
      <button class="btn ghost" type="button" @click="list.resetFilters()">重置条件</button>
    </form>

    <table class="data-table">
      <thead>
        <tr>
          <th v-for="column in config.columns" :key="column">{{ column }}</th>
          <th>可执行动作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in list.rows.value" :key="String(row.id)">
          <td v-for="column in config.columns" :key="column">{{ row[column] ?? '—' }}</td>
          <td class="row-actions">
            <button
              v-for="action in config.actions"
              :key="action"
              class="link"
              type="button"
              @click="runAction(action, row)"
            >
              {{ action }}
            </button>
          </td>
        </tr>
        <tr v-if="!list.rows.value.length">
          <td :colspan="config.columns.length + 1" class="empty-state">{{ config.emptyText }}</td>
        </tr>
      </tbody>
    </table>

    <footer class="page-foot">
      <span>共 {{ list.total.value }} 条{{ config.entityLabel }}记录</span>
      <Pager
        :page="list.page.value"
        :size="list.size.value"
        :total="list.total.value"
        @change-page="list.gotoPage"
        @change-size="list.changeSize"
      />
      <span v-if="list.notice.value" class="notice-text">{{ list.notice.value }}</span>
      <span v-else-if="list.errorMessage.value" class="error-text">{{ list.errorMessage.value }}</span>
    </footer>
  </section>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue'

import Pager from '@/components/Pager.vue'
import { request } from '@/api/client'
import { useModuleList, type ListPayload } from '@/composables/useModuleList'

export interface ModuleConfig {
  module: string
  title: string
  description: string
  entityLabel: string
  exportLabel: string
  emptyText: string
  columns: string[]
  filterFields: string[]
  statuses: string[]
  actions: string[]
  stats: { label: string; value: number }[]
}

const props = defineProps<{ config: ModuleConfig }>()
// 模板里统一叫 config
const config = props.config

const list = useModuleList({ endpoint: `/api/${config.module}`, cacheKey: config.module })

// 输入框只改草稿值；点查询（或回车）才发请求，避免边打字边换条件
const keywordModel = computed({
  get: () => list.keyword.value,
  set: (value: string) => { list.keyword.value = value },
})
const statusModel = computed({
  get: () => list.status.value,
  set: (value: string) => { list.status.value = value },
})
const filtersModel = computed(() => list.filters.value)

function onSearch() {
  list.search()
}

function exportRows() {
  void list.exportRows()
}

function openCreate() {
  list.errorMessage.value = `${config.entityLabel}登记入口尚未接入审批流`
}

async function runAction(action: string, row: ListPayload['items'][number]) {
  list.errorMessage.value = ''
  try {
    const response = await request(`/api/${config.module}/${row.id}/actions`, {
      method: 'POST',
      body: JSON.stringify({ action }),
    })
    if (!response.ok) {
      throw new Error(`${config.entityLabel}动作未生效，请稍后重试`)
    }
    list.refresh()
  } catch (error) {
    list.errorMessage.value = error instanceof Error ? error.message : `${config.entityLabel}操作失败`
  }
}

onMounted(list.restoreOrInit)
</script>
