<script setup lang="ts">
import { ref, watch } from "vue";
import { useRoute } from "vue-router";
import { albumMedia } from "@/features/albums/api";
import { artistMedia } from "@/features/artists/api";
import { search } from "../api";
import { playSong } from "@/features/songs/api";

import SearchItem from "../components/SearchItem.vue";

const route = useRoute();

type SearchResponse = {
  albums: any[];
  artists: any[];
  songs: any[];
};

const data = ref<SearchResponse>({
  albums: [],
  artists: [],
  songs: [],
});

watch(
  () => route.query.q,
  async (query) => {
    if (typeof query === "string") {
      const res = await search(query);
      data.value = res.data;
    }
  },
  { immediate: true },
);
</script>

<template>
  <div class="album-list section m-auto">
    <br /><br />
    <h1 v-if="data.albums.length" class="primary-title">Albums</h1>
    <div class="list__grid">
      <div v-for="album in data.albums" :key="album.public_id">
        <RouterLink class="list__item" :to="{ name: 'album', params: { id: album.public_id } }">
          <SearchItem
            :name="album.name"
            :src="albumMedia.cover(album.public_id)"
            type="Album"
            shape="square"
          />
        </RouterLink>
      </div>
    </div>
    <h1 v-if="data.artists.length" class="primary-title">Artists</h1>
    <div class="list__grid">
      <div v-for="artist in data.artists" :key="artist.public_id">
        <RouterLink
          class="list__item"
          :to="{ name: 'artist', params: { public_id: artist.public_id } }"
        >
          <SearchItem
            :name="artist.name"
            :src="artistMedia.profile(artist.public_id)"
            type="Artist"
          />
        </RouterLink>
      </div>
    </div>
    <h1 v-if="data.songs.length" class="primary-title">Songs</h1>
    <div class="list__grid">
      <div v-for="song in data.songs" :key="song.public_id">
        <button @click="playSong(song.public_id)" class="list__item">
          <SearchItem
            :name="song.name"
            :src="albumMedia.cover(song.album)"
            shape="square"
            type="Song"
          />
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.list__item {
  width: 100%;
}
</style>
