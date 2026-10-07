<template>
  <div class="pager">
    <span class="pager-total">共 {{ total }} 条</span>
    <button class="btn" type="button" :disabled="page <= 1" @click="go(page - 1)">上一页</button>
    <span class="pager-pos">第 {{ page }} / {{ totalPages }} 页</span>
    <button class="btn" type="button" :disabled="page >= totalPages" @click="go(page + 1)">下一页</button>
    <label class="pager-size">
      每页
      <select :value="size" @change="onSizeChange">
        <option v-for="opt in options" :key="opt" :value="opt">{{ opt }}</option>
      </select>
      条
    </label>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  page: number
  size: number
  total: number
  sizeOptions?: number[]
}>(), {
  sizeOptions: () => [10, 20, 50, 100],
})

const emit = defineEmits<{
  (e: 'change-page', page: number): void
  (e: 'change-size', size: number): void
}>()

const options = props.sizeOptions

const totalPages = computed(() => (props.total === 0 ? 1 : Math.ceil(props.total / props.size)))

function go(next: number) {
  if (next < 1 || next > totalPages.value) {
    return
  }
  emit('change-page', next)
}

function onSizeChange(event: Event) {
  emit('change-size', Number((event.target as HTMLSelectElement).value))
}
</script>
