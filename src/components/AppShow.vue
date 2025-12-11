<template>
  <el-input v-model="input" style="width: 240px" placeholder="Please input" />
  <el-button type="primary" style="margin-left: 10px;" @click="submitUserForm">Search</el-button>
</template>


<script lang="ts" setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  const router = useRouter()

  const input = ref('')

  const submitUserForm = () => {
    router.push({ name: 'Painters', query: { search: input.value } })
  }
</script>
