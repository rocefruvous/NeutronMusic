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
  <span class="profile__display-name">{{ name }}</span>
</template>

<style scoped>
.profile__display-name {
  font-weight: 840;
  font-size: 2rem;
}
</style>
