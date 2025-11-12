<template>

  <el-container style="height: 100vh;">
    <el-affix>
      <el-header height="60px"
        style="background-color: #409eff; color: white; line-height: 60px; font-size: 20px; padding-left: 20px;">
        Patient Management System
      </el-header>
    </el-affix>
    <el-main>
      <NavigateBar />
    </el-main>
    <el-footer height="60px"
      style="background-color: #409eff; color: white; line-height: 60px; font-size: 20px; padding-left: 20px;">

    </el-footer>
  </el-container>

</template>

<script lang="ts" setup>
  import NavigateBar from '@/view/navigate-bar.vue'
  import { ElFooter } from 'element-plus';
</script>

<style></style>
