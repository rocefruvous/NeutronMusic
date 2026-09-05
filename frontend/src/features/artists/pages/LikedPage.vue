<script setup lang="ts">
import { ref, watch } from "vue";
import { useRoute } from "vue-router";
import { getLikedSongs, playSong } from "@/features/songs/api";
import { albumMedia } from "@/features/albums/api";

import MediaCard from "@/shared/components/MediaCard.vue";

const route = useRoute();
const data = ref<any>(null);

watch(
  () => route.params.public_id,
  async (id) => {
    if (typeof id === "string") {
      const res = await getLikedSongs(id);
      data.value = res.data;
    }
  },
  { immediate: true },
);
</script>

<template>
  <div class="list__grid">
    <div v-for="song in data" :key="song.public_id" class="album-card">
      <button class="w-full" @click="playSong(song.public_id)">
        <MediaCard
          :name="song.name"
          :src="albumMedia.cover(song.album_details.public_id)"
          :secondary="song.album_details.name"
          type="Song"
          shape="square"
        />
      </button>
    </div>
  </div>
</template>

<style scoped></style>
