<script setup lang="ts">
import { ref, watch } from "vue";
import { useRoute } from "vue-router";
import { getSongs, playSong } from "@/features/songs/api";

const route = useRoute();
const data = ref<any>(null);

watch(
  () => route.params.id,
  async (id) => {
    if (typeof id === "string") {
      const res = await getSongs(id);
      data.value = res.data;
    }
  },
  { immediate: true },
);
</script>

<template>
  <div class="album-list">
    <h1 class="primary-title">Songs</h1>
    <div v-for="song in data" :key="song.public_id" class="song-card">
      <button class="w-full" @click="playSong(song.public_id)">
        <div class="song-card__content text-left p-2 gap-1.5">
          <p>{{ song.track_number }}</p>
          <h3 class="song-card__name">{{ song.name }}</h3>
          <p>{{ song.duration }}</p>
        </div>
      </button>
    </div>
  </div>
</template>

<style scoped>
.album-card {
  background: transparent;
  width: 13rem;
  border-radius: 1rem;
}

.song-card__content {
  display: grid;
  grid-template-columns: 1em 1fr 1fr;
  font-size: 1.2em;
  border-radius: 1rem;
  transition: 200ms;
  color: var(--foreground-muted);
}

.song-card__content:hover {
  background-color: var(--surface);
}

.album-card:hover {
  background: var(--surface);
}

.album-card__cover-art {
  width: 12rem;
  border-radius: 1rem;
}
.song-card__name {
  font-weight: 750;
  color: var(--foreground);
}
</style>
