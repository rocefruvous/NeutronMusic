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
    <div class="media-card">
      <div class="media-card__content text-left">
        <img class="media-card__cover-art" :src="props.src" />
        <h3 class="media-card__name">{{ props.name }}</h3>
        <p class="text-muted">{{ props.secondary }}</p>
      </div>
    </div>
  </component>
</template>

<style scoped>
.media-card {
  background: transparent;
  width: 13rem;
  border-radius: 1rem;
}

.media-card__content {
  padding: 1rem;
}

.media-card:hover {
  background: var(--surface);
}

.media-card__cover-art {
  width: 12rem;
  border-radius: 1rem;
}
.media-card__name {
  font-size: 1.2em;
  font-weight: 700;
}
</style>
