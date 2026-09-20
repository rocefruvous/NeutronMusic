<script setup lang="ts">
import { RouterLink } from "vue-router";

const props = defineProps({
  to: String,
  disabled: Boolean,
  name: String,
  secondary: String,
  src: String,
});
</script>

<template>
  <component :is="to ? RouterLink : 'button'" :to="to" :disabled="disabled">
    <div class="media-card cursor-pointer">
      <div class="media-card__content text-left">
        <img class="media-card__cover-art" :src="props.src" />
        <h3 class="text-lg">{{ props.name }}</h3>
        <p class="media-card__secondary">{{ props.secondary }}</p>
      </div>
    </div>
  </component>
</template>

<style scoped>
a {
  text-decoration: none;
}

.media-card {
  color: var(--foreground-secondary);
  background: transparent;
  width: 13rem;
  border-radius: 1rem;
}

.media-card__secondary {
  color: var(--foreground-muted);
  transition: 200ms;
}

.media-card:hover .media-card__content {
  color: var(--foreground);
}

.media-card:hover .media-card__secondary {
  color: var(--foreground-secondary);
}

.media-card__content {
  transition: 200ms;
  padding: 1rem;
}

.media-card__cover-art {
  width: 12rem;
  border-radius: 0;
}
</style>
