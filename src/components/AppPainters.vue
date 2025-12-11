<template>
  <li>{{ search }}</li>
  <el-table-v2 :columns="columns" :data="tableRows" :width="700" :height="400" fixed />

</template>

<script lang="ts" setup>
  import { ref, watchEffect } from 'vue'
  import apiClient from '@/api/axios'
  import type { PainterRow, PaintersResponse } from '@/types/painter'

  const columns = [
    { key: 'name', dataKey: 'name', title: '姓名', width: 160 },
    { key: 'account', dataKey: 'account', title: '账户', width: 140 },
    { key: 'date', dataKey: 'date', title: '日期', width: 180 },
    { key: 'gender', dataKey: 'gender', title: '性别', width: 120 },
  ]

  const props = defineProps(['search'])

  const tableRows = ref<Array<{ name: string; account: string; date: string; gender: string }>>([])

  const fetchPainters = async (search?: string) => {
    try {
      const response = await apiClient.get<PaintersResponse>('painters', { params: { search } })
      const painters: PainterRow[] = response.data?.painters ?? []
      const mapped = painters.map(([name, account, date, gender]) => ({ name, account, date, gender }))
      console.log('Mapped painters:', mapped)
      tableRows.value = mapped
    } catch (error) {
      console.error('There was an error!', error)
      tableRows.value = []
    }
  }

  watchEffect(() => {
    fetchPainters(props.search)
  })

</script>
