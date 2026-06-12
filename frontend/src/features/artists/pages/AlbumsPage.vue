<script setup lang="ts">
import { ref, watch } from "vue";
import { useRoute } from "vue-router";
import { getAlbums, albumMedia } from "@/features/albums/api";

import MediaCard from "@/shared/components/MediaCard.vue";

const route = useRoute();
const data = ref<any>(null);

watch(
  () => route.params.public_id,
  async (id) => {
    if (typeof id === "string") {
      const res = await getAlbums(id);
      data.value = res.data;
    }
  },
  { immediate: true },
);
</script>

<template>
  <div class="grid grid-cols-3">
    <div v-for="album in data" :key="album.public_id">
      <MediaCard
        :to="{ name: 'album', params: { id: album.public_id } }"
        :src="albumMedia.cover(album.public_id)"
        :name="album.name"
        :secondary="album.release_date"
      />
    </div>
  </div>
</template>

<style scoped></style>
