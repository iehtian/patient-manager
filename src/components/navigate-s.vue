<template>
  <el-icon>
    <location />
  </el-icon>
  <span>{{ title }}</span>
</template>

<script lang="ts" setup>
  defineProps<{ title: string }>()
</script>
