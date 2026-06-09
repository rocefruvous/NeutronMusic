<script setup lang="ts">
import { ref, watch } from "vue";
import { useRoute } from "vue-router";
import { getAlbums, albumMedia } from "@/features/albums/api";

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
  <div class="album-list">
    <div v-for="album in data" :key="album.public_id" class="album-card">
      <RouterLink :to="{ name: 'album', params: { id: album.public_id } }">
        <div class="album-card__content">
          <img class="album-card__cover-art" :src="albumMedia.cover(album.public_id)" />
          <h3 class="album-card__name">{{ album.name }}</h3>
          <p>{{ album.release_date }}</p>
        </div>
      </RouterLink>
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
