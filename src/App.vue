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
  import AppInput from '@/components/AppShow.vue'
  import { useRouter } from 'vue-router'
  import type { PainterRow } from '@/types/painter'

  const router = useRouter()

  const show_painter = (data: PainterRow[]) => {
    console.log('Received search results in App.vue:', data)
    router.push({ name: 'Painters', state: { data } })
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
