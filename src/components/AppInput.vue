<template>
  <el-input v-model="input" style="width: 240px" placeholder="Please input" />
  <el-button type="primary" style="margin-left: 10px;" @click="submitUserForm">Search</el-button>
</template>

<script lang="ts" setup>
  import { ref, watch } from 'vue'
  const input = ref('')
  import apiClient from '@/api/axios';
  const Search_res = ref<unknown[][]>([])
  const submitUserForm = () => {
    return apiClient.get('painters')
      .then((response) => {
        Search_res.value = response.data
        console.log(Search_res.value);
      })
      .catch((error) => {
        console.error('There was an error!', error);
      })
  }
  const emit = defineEmits<{
    (e: 'update:search-results', value: unknown[][]): void
  }>()
  watch(Search_res, (newVal) => {
    console.log('Search results updated:', newVal);
    emit('update:search-results', newVal)
  })
</script>
