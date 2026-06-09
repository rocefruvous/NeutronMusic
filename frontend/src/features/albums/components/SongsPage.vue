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
    <div v-for="song in data" :key="song.public_id" class="song-card">
      <button @click="playSong(song.public_id)">
        <div class="album-card__content flex flex-row gap-1.5">
          <p>{{ song.track_number }}</p>
          <h3 class="album-card__name">{{ song.name }}</h3>
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

.album-card__content {
  padding: 1rem;
}

.album-card:hover {
  background: var(--surface);
}

.album-card__cover-art {
  width: 12rem;
  border-radius: 1rem;
}
.album-card__name {
  font-size: 1.2em;
  font-weight: 700;
}
</style>
