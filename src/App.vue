<template>

  <el-container style="height: 100vh;">
    <el-affix>
      <el-header class="nav">
        Patient Management System
        <AppInput />
      </el-header>
    </el-affix>
    <el-main>
      <NavigateBar />
    </el-main>
    <el-footer class="nav">

    </el-footer>
  </el-container>

</template>

<script lang="ts" setup>
  import NavigateBar from '@/view/navigate-bar.vue'
  import AppInput from '@/components/AppInput.vue'


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
