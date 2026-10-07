<template>
  <section class="page" :data-module="config.module">
    <header class="page-head">
      <div>
        <h2>{{ config.title }}</h2>
        <p class="page-desc">{{ config.desc }}</p>
      </div>
      <div class="page-actions">
        <button class="btn primary" type="button" @click="openCreate">登记{{ config.label }}</button>
        <button class="btn" type="button" @click="exportRows">导出{{ config.label }}清单</button>
      </div>
    </header>

    <div class="stat-row">
      <article v-for="item in config.stats" :key="item.label" class="stat-card">
        <span class="stat-label">{{ item.label }}</span>
        <strong class="stat-value">{{ item.value }}</strong>
      </article>
    </div>

    <form class="filter-bar" @submit.prevent="applyFilters">
      <label class="filter-item">
        <span>{{ config.keywordLabel }}</span>
        <input v-model="keyword" :placeholder="`按${config.keywordLabel}检索`" />
      </label>
      <label class="filter-item">
        <span>状态</span>
        <select v-model="status">
          <option value="">全部状态</option>
          <option v-for="item in config.statuses" :key="item" :value="item">{{ item }}</option>
        </select>
      </label>
      <button class="btn" type="submit">查询</button>
      <button class="btn ghost" type="button" @click="resetFilters">重置条件</button>
      <button class="btn ghost" type="button" @click="toggleOrder">
        登记时间{{ order === 'desc' ? '最新在前 ↓' : '最早在前 ↑' }}
      </button>
    </form>

    <table class="data-table">
      <thead>
        <tr>
          <th v-for="column in config.columns" :key="column">{{ column }}</th>
          <th>登记时间</th>
          <th>可执行动作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in rows" :key="String(row.id)">
          <td v-for="column in config.columns" :key="column">{{ row[column] ?? '—' }}</td>
          <td>{{ row.created_at ?? '—' }}</td>
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
        <tr v-if="!rows.length && loading">
          <td :colspan="config.columns.length + 2" class="empty-state">加载中…</td>
        </tr>
        <tr v-if="!rows.length && !loading">
          <td :colspan="config.columns.length + 2" class="empty-state">暂无{{ config.label }}数据，可先登记{{ config.label }}</td>
        </tr>
      </tbody>
    </table>

    <footer class="page-foot">
      <span>共 {{ total }} 条{{ config.label }}记录</span>
      <div class="pager">
        <button class="btn ghost" type="button" :disabled="page <= 1 || loading" @click="changePage(page - 1)">上一页</button>
        <span class="pager-status">第 {{ page }} / {{ maxPage }} 页</span>
        <button class="btn ghost" type="button" :disabled="page >= maxPage || loading" @click="changePage(page + 1)">下一页</button>
        <select class="pager-size" :value="size" @change="onSizeChange">
          <option v-for="option in sizeOptions" :key="option" :value="option">每页 {{ option }} 条</option>
        </select>
      </div>
    </footer>
    <p v-if="notice" class="list-message notice-text">{{ notice }}</p>
    <p v-if="errorMessage" class="list-message error-text">{{ errorMessage }}</p>
  </section>
</template>

<script setup lang="ts">
import { useListPage, type ListPageConfig } from '@/composables/useListPage'

const props = defineProps<{ config: ListPageConfig }>()

const {
  keyword,
  status,
  order,
  page,
  size,
  total,
  rows,
  notice,
  errorMessage,
  loading,
  maxPage,
  applyFilters,
  resetFilters,
  changePage,
  changeSize,
  toggleOrder,
  exportRows,
  runAction,
} = useListPage(props.config)

const sizeOptions = [10, 20, 50, 100]

function onSizeChange(event: Event) {
  changeSize(Number((event.target as HTMLSelectElement).value))
}

function openCreate() {
  errorMessage.value = `${props.config.label}登记入口尚未接入审批流`
}
</script>
