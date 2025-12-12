<template>
  <li>{{ search }}</li>
  <el-table-v2 :columns="columns" :data="tableRows" :width="700" :height="400" fixed />

</template>

<script lang="ts" setup>
  import { ref, watchEffect } from 'vue'
  import apiClient from '@/api/axios'
  import type { patientRow, patientsResponse } from '@/types/patient'

  const columns = [
    { key: 'name', dataKey: 'name', title: '姓名', width: 160 },
    { key: 'date', dataKey: 'date', title: '出生日期', width: 180 },
    { key: 'gender', dataKey: 'gender', title: '性别', width: 120 },
  ]

  const props = defineProps(['search'])

  const tableRows = ref<Array<{ name: string; date: string; gender: string }>>([])

  const fetchpatients = async (search?: string) => {
    try {
      const response = await apiClient.get<patientsResponse>('patients', { params: { search } })
      const patients: patientRow[] = response.data?.patients ?? []
      console.log('Fetched patients:', patients)
      const mapped = patients.map((item) => {
        const [, name, birthDate, gender] = item
        return { name, date: birthDate, gender }
      })
      console.log('Mapped patients:', mapped)
      tableRows.value = mapped
    } catch (error) {
      console.error('There was an error!', error)
      tableRows.value = []
    }
  }

  watchEffect(() => {
    fetchpatients(props.search)
  })

</script>
