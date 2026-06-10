<script setup lang="ts">
import { ref, watch } from "vue";
import { useRoute } from "vue-router";
import { getLikedSongs } from "@/features/songs/api";
import { albumMedia } from "@/features/albums/api";

import SongItem from "../components/SongItem.vue";

const route = useRoute();
const data = ref<any>(null);

watch(
  () => route.params.public_id,
  async (id) => {
    if (typeof id === "string") {
      const res = await getArtistSongs(id);
      data.value = res.data;
    }
  },
  { immediate: true },
);
</script>

<template>
  <div class="list__grid">
    <div v-for="song in data" :key="song.public_id" class="album-card">
      <RouterLink :to="{ name: 'album', params: { id: song.public_id } }">
        <SongItem
          :name="song.name"
          :src="albumMedia.cover(song.album)"
          type="Song"
          shape="square"
        />
      </RouterLink>
    </div>
  </div>
</template>

<style scoped>
.album-card {
  background: transparent;
  width: 100%;
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
