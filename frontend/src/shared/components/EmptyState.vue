<script setup lang="ts">
const props = defineProps({
  title: String,
  message: String,
});
</script>

<template>
  <div class="w-screen h-screen flex justify-center items-center">
    <div>
      <h2 class="primary-title">{{ props.title }}</h2>
      <p>{{ props.message }}</p>
    </div>
  </div>
</template>

<style scoped></style>
