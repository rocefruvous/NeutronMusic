<script setup lang="ts">
import { onMounted, ref, watchEffect } from "vue";

import { getRecommendations } from "../api";

import { artistMedia } from "@/features/artists/api";
import { albumMedia } from "@/features/albums/api";
import { playSong } from "@/features/songs/api";

import MediaCard from "@/shared/components/MediaCard.vue";

type SearchResponse = {
  topSongs: any[];
  featuredArtists: any[];
  albums: any[];
  recentAlbums: any[];
};

const data = ref<SearchResponse>({
  topSongs: [],
  featuredArtists: [],
  albums: [],
  recentAlbums: [],
});

async function fetchBrowse() {
  const { data: res } = await getRecommendations();
  data.value = res;
  console.log(data);
}

onMounted(() => {
  fetchBrowse();
});
</script>

<template>
  <div class="home-page__banner flex justify-center h-96">
    <span class="section w-full">
      <h1 class="home-page__title">what are you listening to today?</h1>
    </span>
  </div>
  <div class="flex justify-center">
    <div class="section">
      <h2 class="primary-title">Top Songs</h2>
      <div class="grid grid-cols-5">
        <div v-for="song in data.topSongs" :key="song.public_id">
          <MediaCard
            @click="playSong(song.public_id)"
            :name="song.name"
            :secondary="song.album_details.name"
            :src="albumMedia.cover(song.album_details.public_id)"
          />
        </div>
      </div>

      <h2 class="primary-title">Featured Artists</h2>
      <div class="grid grid-cols-5">
        <div v-for="artist in data.featuredArtists" :key="artist.public_id">
          <MediaCard
            :to="{ name: 'artist', params: { public_id: artist.public_id } }"
            :name="artist.name"
            secondary="Artist"
            :src="artistMedia.profile(artist.public_id)"
          />
        </div>
      </div>

      <h2 class="primary-title">Albums</h2>
      <div class="grid grid-cols-5">
        <div v-for="album in data.albums" :key="album.public_id">
          <MediaCard
            :to="{ name: 'album', params: { id: album.public_id } }"
            :name="album.name"
            :secondary="album.artist_details.name"
            :src="albumMedia.cover(album.public_id)"
          />
        </div>
      </div>

      <h2 class="primary-title">Recent Albums</h2>
      <div class="grid grid-cols-5">
        <div v-for="album in data.recentAlbums" :key="album.public_id">
          <MediaCard
            :to="{ name: 'album', params: { id: album.public_id } }"
            :name="album.name"
            :secondary="album.artist_details.name"
            :src="albumMedia.cover(album.public_id)"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-page__title {
  font-size: 3.5em;
  font-weight: 800;
}
.home-page__banner {
  padding: 5rem;
  background-size: cover;
  background-image:
    linear-gradient(rgba(0, 0, 0, 0.2), var(--background)), url(/src/assets/images/banner.png);
}
</style>
