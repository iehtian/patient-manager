<template>
  <div>
    <li v-if="search">搜索条件：{{ search }}</li>
    <el-table-v2 v-if="!loading && tableRows.length" :columns="columns" :data="tableRows" :width="700" :height="400"
      fixed :row-event-handlers="rowEventHandlers" />
    <p v-else-if="loading">查询中...</p>
    <p v-else-if="search">未查询到患者</p>
    <p v-else>请输入搜索条件</p>
  </div>
</template>
<script lang="ts" setup>
  import { ref, watch } from 'vue'
  import { useRoute } from 'vue-router'
  import apiClient from '@/api/axios'
  import type { patientRow, patientsResponse } from '@/types/patient'

  const route = useRoute()

  const search = ref<string | undefined>(undefined)
  const loading = ref(false)

  const columns = [
    { key: 'name', dataKey: 'name', title: '姓名', width: 160 },
    { key: 'date', dataKey: 'date', title: '出生日期', width: 180 },
    { key: 'gender', dataKey: 'gender', title: '性别', width: 120 },
  ]

  const tableRows = ref<Array<{ name: string; date: string; gender: string }>>([])

  const fetchPatients = async (search?: string) => {
    if (!search) {
      tableRows.value = []
      loading.value = false
      return
    }

    loading.value = true
    try {
      const response = await apiClient.get<patientsResponse>('patients', {
        params: { search }
      })

      const patients: patientRow[] = response.data?.patients ?? []

      tableRows.value = patients.map((item) => {
        const [, name, birthDate, gender] = item
        return { name, date: birthDate, gender }
      })
    } catch (error) {
      console.error(error)
      tableRows.value = []
    } finally {
      loading.value = false
    }
  }

  watch(
    () => route.query.search,
    (val) => {
      search.value = val as string | undefined
      fetchPatients(search.value)
    },
    { immediate: true }
  )
  const rowEventHandlers = {
    onClick: ({ rowData }: { rowData: { name: string } }) => {
      console.log('Row clicked:', rowData)
    }
  }

</script>
