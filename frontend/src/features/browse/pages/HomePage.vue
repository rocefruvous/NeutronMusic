<script setup lang="ts">
import { onMounted, ref, watchEffect } from "vue";

import { getRecommendations } from "../api";

import { artistMedia } from "@/features/artists/api";
import { albumMedia } from "@/features/albums/api";
import { playSong } from "@/features/songs/api";

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
          <button @click="playSong(song.public_id)" class="list__item">
            <div class="album-card__content">
              <img class="album-card__cover-art" :src="albumMedia.cover(song.album)" />
              <h3 class="album-card__name">{{ song.name }}</h3>
              <p class="text-muted">Song</p>
            </div>
          </button>
        </div>
      </div>

      <h2 class="primary-title">Featured Artists</h2>
      <div class="grid grid-cols-5">
        <div v-for="artist in data.featuredArtists" :key="artist.public_id">
          <RouterLink
            class="list__item"
            :to="{ name: 'artist', params: { public_id: artist.public_id } }"
          >
            <div class="album-card__content">
              <img class="album-card__cover-art" :src="artistMedia.profile(artist.public_id)" />
              <h3 class="album-card__name">{{ artist.name }}</h3>
              <p class="text-muted">Artist</p>
            </div>
          </RouterLink>
        </div>
      </div>

      <h2 class="primary-title">Albums</h2>
      <div class="grid grid-cols-5">
        <div v-for="album in data.albums" :key="album.public_id">
          <RouterLink class="list__item" :to="{ name: 'album', params: { id: album.public_id } }">
            <div class="album-card__content">
              <img class="album-card__cover-art" :src="albumMedia.cover(album.public_id)" />
              <h3 class="album-card__name">{{ album.name }}</h3>
              <p class="text-muted">Album</p>
            </div>
          </RouterLink>
        </div>
      </div>

      <h2 class="primary-title">Recent Albums</h2>
      <div class="grid grid-cols-5">
        <div v-for="album in data.recentAlbums" :key="album.public_id">
          <RouterLink class="list__item" :to="{ name: 'album', params: { id: album.public_id } }">
            <div class="album-card__content">
              <img class="album-card__cover-art" :src="albumMedia.cover(album.public_id)" />
              <h3 class="album-card__name">{{ album.name }}</h3>
              <p class="text-muted">Album</p>
            </div>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.album-card__content {
  padding: 1rem;
}

.album-card:hover {
  background: var(--surface);
}

.album-card__cover-art {
  width: 12rem;
  border-radius: 1rem;
  background-image: url(/src/assets/images/default_avatar.jpg);
  background-size: cover;
}
.album-card__name {
  font-size: 1.2em;
  font-weight: 700;
}

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
