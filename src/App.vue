<template>

  <el-container style="height: 100vh;">
    <el-affix>
      <el-header class="nav">
        Patient Management System
        <AppInput />
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
  import AppInput from '@/components/AppSearchPatient.vue'

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
