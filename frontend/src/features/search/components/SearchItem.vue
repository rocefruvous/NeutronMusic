<script setup lang="ts">
const props = withDefaults(
  defineProps<{
    name: string;
    type: string;
    src: string;
    shape?: "circle" | "square";
  }>(),
  {
    shape: "circle",
  },
);
</script>

<template>
  <div class="card flex flex-row gap-1.5">
    <img class="avatar avatar--medium" :class="props.shape" :src="src" :alt="name" />
    <div class="content-center text-left">
      <h3 class="card__name">{{ name }}</h3>
      <p>{{ type }}</p>
    </div>
  </div>
</template>

<style scoped>
.card {
  padding: 1rem;
  border-radius: 1rem;
}

.card:hover {
  background: var(--surface);
}

.card__name {
  font-size: 1.2em;
  font-weight: 700;
}
</style>
