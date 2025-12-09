<template>
  <el-input v-model="input" style="width: 240px" placeholder="Please input" />
  <el-button type="primary" style="margin-left: 10px;" @click="submitUserForm">Search</el-button>
</template>


<script lang="ts" setup>
  import { ref } from 'vue'
  import apiClient from '@/api/axios'
  import type { PainterRow, PaintersResponse } from '@/types/painter'

  const input = ref('')
  const Search_res = ref<PainterRow[]>([])
  const emit = defineEmits<{
    'update:search-results': [PainterRow[]]
  }>()

  const submitUserForm = () => {
    return apiClient
      .get<PaintersResponse>('painters')
      .then((response) => {
        console.log('Response data:', response.data)
        const painters = response.data?.painters ?? []
        Search_res.value = painters
        emit('update:search-results', painters)
      })
      .catch((error) => {
        console.error('There was an error!', error)
      })
  }
</script>
