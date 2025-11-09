<template>
  <div class="Person">
    <h1>
      姓名:{{ name }} 年龄:{{ age }}
    </h1>
  </div>
</template>

<script lang="ts">
export default {
  name: 'PersonCard',
  data() {
    return {
      name: '张三',
      age: 18
    }
  }
}
</script>

<style scoped>
.Person {
  font-size: 20px;
  color: #333;
}
</style>
