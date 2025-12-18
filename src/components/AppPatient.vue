<template>
  <div>
    <li v-if="search">搜索条件：{{ search }}</li>
    <el-table v-if="!loading && tableRows.length" :data="tableRows" :width="700" :height="400" @row-click="turn2Detail"
      @cell-mouse-enter="handleCellMouseEnter">
      <el-table-column prop="order" label="编号" width="120" />
      <el-table-column prop="name" label="姓名" width="120" />
      <el-table-column prop="birthDate" label="出生日期" width="120" />
      <el-table-column prop="gender" label="性别" width="320" />
    </el-table>
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
  type TableRow_t = { order: string; name: string; birthDate: string; gender: string }
  const tableRows = ref<Array<TableRow_t>>([])

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
      console.log(patients)
      tableRows.value = patients.map((item) => {
        const [order, name, birthDate, gender] = item
        return { order, name, birthDate, gender }
      })
      console.log(tableRows.value)
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
  const turn2Detail = (row: TableRow_t) => {
    console.log('点击了行', row)
  }
  const handleCellMouseEnter = (row: TableRow_t) => {
    console.log('鼠标移入行:', row)
  }
</script>
