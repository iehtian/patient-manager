<template>
  <el-table-v2 :columns="columns" :data="tableRows" :width="700" :height="400" fixed />
</template>

<script lang="ts" setup>
  import { computed } from 'vue'
  import { useRouter } from 'vue-router'
  import type { PainterRow } from '@/types/painter'

  const columns = [
    { key: 'name', dataKey: 'name', title: '姓名', width: 160 },
    { key: 'account', dataKey: 'account', title: '账户', width: 140 },
    { key: 'date', dataKey: 'date', title: '日期', width: 180 },
    { key: 'gender', dataKey: 'gender', title: '性别', width: 120 },
  ]

  const router = useRouter()

  const tableRows = computed(() => {
    const payload = (
      (router.options.history.state as { data?: PainterRow[] } | null)?.data ?? []
    )
    return payload.map((row, idx) => ({
      id: idx,
      name: row[0],
      account: row[1],
      date: row[2],
      gender: row[3],
    }))
  })
</script>
