<script setup lang="ts">
import { Play, Pause, Heart } from "@lucide/vue";

import { ref, watch, computed } from "vue";

import { API_BASE } from "@/api/client";
import { endpoints } from "@/api/endpoints";
import { audioState } from "./state";

import { getSong } from "@/features/songs/api";
import { getAlbum, albumMedia } from "@/features/albums/api";
import { getArtist } from "@/features/artists/api";

import { useAudioPlayer } from "./composables/useAudioPlayer";

const src = computed(() =>
  audioState.songId ? `${API_BASE}${endpoints.stream}${audioState.songId}` : "",
);

const { audio, currentTime, duration, isPlaying, togglePlay, seek } = useAudioPlayer(
  () => src.value,
);

const songData = ref<Song | null>(null);
const albumData = ref<Album | null>(null);
const artistData = ref<Artist | null>(null);

watch(
  () => audioState.songId,
  async (id) => {
    songData.value = albumData.value = artistData.value = null;
    if (!id) return;

    const song = await getSong(id);
    songData.value = song;

    if (!song.album) return;
    const album = (await getAlbum(song.album)).data;
    albumData.value = album;

    if (!album.artist) return;
    artistData.value = (await getArtist(album.artist)).data;
  },
  { immediate: true },
);

const fmt = (t: number) =>
  `${(t / 60) | 0}:${Math.floor(t % 60)
    .toString()
    .padStart(2, "0")}`;
</script>

<template>
  <audio ref="audio" :src="src"></audio>
  <div id="player" class="fixed bottom-0 w-full">
    <div class="absolute w-full top-0 left-0 -translate-y-2/4 flex flex-row justify-center">
      <div class="duration__frame flex flex-row w-full justify-center gap-4">
        <div
          class="current-time flex flex-row absolute top-0 -translate-y-full w-full justify-between px-5"
        >
          <p>{{ fmt(currentTime) }}</p>
          <p>{{ fmt(duration) }}</p>
        </div>

        <input
          id="duration"
          class="w-full"
          type="range"
          min="0"
          :max="duration"
          :value="currentTime"
          @input="seek"
        />
      </div>
    </div>
    <div class="flex flex-row p-3">
      <div class="flex flex-row gap-2">
        <img
          v-if="songData?.album"
          :src="albumMedia.cover(songData.album)"
          class="avatar avatar--medium square"
        />
        <div class="content-center">
          <p class="bold-text whitespace-nowrap">{{ songData?.name }}</p>
          <span class="flex flex-row gap-0.5">
            <p class="whitespace-nowrap">{{ artistData?.name }}</p>
            -
            <p class="bold-text whitespace-nowrap">{{ albumData?.name }}</p>
          </span>
        </div>
      </div>
      <div class="flex flex-col w-full justify-center">
        <div class="absolute left-1/2 right-1/2 flex flex-row justify-center gap-5">
          <button>
            <div class="player__button player__like-button">
              <Heart />
            </div>
          </button>
          <button @click="togglePlay">
            <div class="player__button player__play-button">
              <Pause :size="36" v-if="isPlaying" />
              <Play :size="36" v-else />
            </div>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
#player {
  background: var(--background);
}

.player__button {
  padding: 0.5rem;
  border-radius: 999rem;
  transition: 200ms;
  cursor: pointer;
}

.player__play-button {
  background-color: rgb(239, 234, 251);
  color: rgb(39, 39, 52);
}

.player__play-button:hover {
  background-color: var(--foreground);
}

.player__like-button {
  background-color: var(--surface);
}

#duration {
  background: transparent;
}
#duration::-moz-range-track {
  background-color: var(--surface);
  height: 2px;
  border-radius: 100vw;
}
#duration::-moz-range-progress {
  background-color: var(--foreground);
  height: 2px;
  border-radius: 100vw;
}
#duration::-moz-range-thumb {
  background-color: transparent;
  border: none;
  height: 12px;
  width: 12px;
  transition: 200ms;
}

.duration__frame:hover #duration::-moz-range-thumb {
  background-color: var(--foreground);
}

.duration__frame:hover .current-time {
  color: var(--foreground-muted);
}

.current-time {
  pointer-events: none;
  color: transparent;
  transition: 200ms;
}
</style>
