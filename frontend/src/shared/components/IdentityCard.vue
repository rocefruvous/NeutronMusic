<script setup lang="ts">
const props = withDefaults(
  defineProps<{
    name: string;
    src: string;
    shape?: "circle" | "square";
  }>(),
  {
    shape: "circle",
  },
);
</script>

<template>
  <div class="relative h-22">
    <div class="inline">
      <img class="avatar absolute bottom-0" :class="props.shape" :src="src" :alt="name" />
    </div>
  </div>
  <h2 class="primary-title my-5">{{ name }}</h2>
</template>

<style scoped></style>
