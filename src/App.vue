<template>

  <el-container style="height: 100vh;">
    <el-affix>
      <el-header class="nav">
        Patient Management System
        <AppInput @update:search-results="show_painter" />
      </el-header>
    </el-affix>
    <el-main>
      <RouterView></RouterView>
    </el-main>
    <el-footer class="nav">

    </el-footer>
  </el-container>

</template>

<script lang="ts" setup>
  import AppInput from '@/components/AppInput.vue'
  import { ref, provide } from 'vue'
  import { useRouter } from 'vue-router'
  const router = useRouter()
  const painterData = ref<unknown[][]>([])
  provide('painterData', painterData)
  const show_painter = (data: unknown[][]) => {
    console.log('Received search results in App.vue:', data)
    painterData.value = data
    router.push({ path: '/ShowPainter' })
  }

</script>

<style>
  .nav {
    background-color: #409eff;
    color: white;
    line-height: 60px;
    font-size: 20px;
    padding-left: 20px;
    border-radius: 10px;
  }
</style>
