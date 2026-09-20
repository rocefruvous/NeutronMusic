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
    <h1 class="songs__title text-2xl font-semibold">Songs</h1>
    <div v-for="song in data" :key="song.public_id" class="song-card">
      <button class="w-full" @click="playSong(song.public_id)">
        <div class="song-card__content text-lg text-left p-2 gap-1.5 cursor-pointer">
          <p class="song-card__number">{{ song.track_number }}</p>
          <h3 class="song-card__name">{{ song.name }}</h3>
        </div>
      </button>
    </div>
  </div>
</template>

<style scoped>
.songs__title {
  color: var(--foreground-muted);
  padding: 0.4rem 1.3rem;

  transition: color 200ms;
}

.song-card__content {
  display: grid;
  grid-template-columns: 1em 1fr 1fr;
  border-radius: 1rem;
  color: var(--foreground-muted);
}

.song-card__name {
  color: var(--foreground-secondary);
  transition: 200ms;
}

.song-card__number {
  transition: 200ms;
}

.song-card:hover .song-card__name {
  color: var(--foreground);
}

.song-card:hover .song-card__number {
  color: var(--foreground-secondary);
}
</style>
