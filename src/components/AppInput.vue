<template>
  <el-input v-model="input" style="width: 240px" placeholder="Please input" />
  <el-button type="primary" style="margin-left: 10px;" @click="submitUserForm">Search</el-button>
</template>

<script lang="ts" setup>
  import { ref } from 'vue'
  const input = ref('')
  import apiClient from '@/api/axios';
  const Search_res = ref<unknown[][]>([])
  const submitUserForm = () => {
    return apiClient.get('painters')
      .then((response) => {
        console.log('Response data:', response.data);
        Search_res.value = response.data
      })
      .catch((error) => {
        console.error('There was an error!', error);
      })
  }
</script>
