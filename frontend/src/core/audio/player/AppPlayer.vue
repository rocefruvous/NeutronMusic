<script setup lang="ts">
import { Play, Pause, Heart } from "@lucide/vue";

import { ref, watch, computed } from "vue";

import { API_BASE } from "@/api/client";
import { endpoints } from "@/api/endpoints";
import { audioState } from "./state";

import { getSong, likeSong } from "@/features/songs/api";
import { albumMedia } from "@/features/albums/api";

import { useAudioPlayer } from "./composables/useAudioPlayer";

const src = computed(() =>
  audioState.songId ? `${API_BASE}${endpoints.stream}${audioState.songId}` : "",
);

const { audio, currentTime, duration, isPlaying, togglePlay, seek } = useAudioPlayer(
  () => src.value,
);

const progress = computed(() => {
  if (!duration.value) return 0;
  return (currentTime.value / duration.value) * 100;
});
const onSeek = (e: Event) => {
  seek(Number((e.target as HTMLInputElement).value));
};

const songData = ref<Song | null>(null);

watch(
  () => audioState.songId,
  async (id) => {
    songData.value = null;
    if (!id) return;

    songData.value = await getSong(id);
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
          step="0.5"
          :style="{ '--progress': `${progress}%` }"
          :max="duration"
          :value="currentTime"
          @input="onSeek"
        />
      </div>
    </div>
    <div class="flex flex-row p-3">
      <div class="flex flex-row gap-2">
        <div class="player__cover-frame">
          <img
            v-if="songData?.album_details.public_id"
            :src="albumMedia.cover(songData.album_details.public_id)"
            class="player__cover-image"
          />
        </div>

        <div class="content-center">
          <p class="bold-text whitespace-nowrap">{{ songData?.name }}</p>
          <span class="flex flex-row gap-0.5">
            <RouterLink
              v-if="songData?.album_details?.artist_details"
              :to="{
                name: 'artist',
                params: {
                  public_id: songData.album_details.artist_details.public_id,
                },
              }"
            >
              <p class="whitespace-nowrap">
                {{ songData.album_details.artist_details.name }}
              </p>
            </RouterLink>

            -

            <RouterLink
              v-if="songData?.album_details"
              :to="{
                name: 'album',
                params: {
                  id: songData.album_details.public_id,
                },
              }"
            >
              <p class="bold-text whitespace-nowrap">
                {{ songData.album_details.name }}
              </p>
            </RouterLink>
          </span>
        </div>
      </div>
      <div class="flex flex-col w-full justify-center">
        <div class="absolute left-1/2 right-1/2 flex flex-row justify-center gap-5">
          <button @click="likeSong(songData.public_id)">
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

.player__cover-frame {
  width: 4.5rem;
  height: 4.5rem;
  background: url("/src/assets/images/default_avatar.jpg") center / cover no-repeat;
  pointer-events: none;
  border-radius: 0.4rem;
  overflow: hidden;
}

.player__cover-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: inherit;
}

.player__button {
  padding: 0.5rem;
  border-radius: 999rem;
  cursor: pointer;
  transition:
    background-color 200ms ease,
    color 200ms ease;
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

/* Progress slider */
#duration {
  --progress: 0%;

  width: 100%;
  height: 2px;
  appearance: none;
  -webkit-appearance: none;

  background: linear-gradient(
    to right,
    var(--foreground) 0%,
    var(--foreground) var(--progress),
    var(--surface) var(--progress),
    var(--surface) 100%
  );

  border-radius: 999px;
  cursor: pointer;
}

/* Firefox */
#duration::-moz-range-track {
  height: 2px;
  background: transparent;
  border-radius: 999px;
}

#duration::-moz-range-progress {
  height: 2px;
  background: transparent;
}

#duration::-moz-range-thumb {
  width: 12px;
  height: 12px;
  background: transparent;
  border: none;
  border-radius: 50%;
  transition: background-color 200ms ease;
}

/* Chromium */
#duration::-webkit-slider-runnable-track {
  height: 2px;
  background: transparent;
  border-radius: 999px;
}

#duration::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;

  width: 12px;
  height: 12px;

  margin-top: -5px;

  background: var(--foreground);
  border-radius: 50%;
  border: none;

  cursor: pointer;
  opacity: 0;
  transition: opacity 200ms ease;
}

.duration__frame:hover #duration::-webkit-slider-thumb {
  opacity: 1;
}

.duration__frame:hover #duration::-webkit-slider-thumb,
.duration__frame:hover #duration::-moz-range-thumb {
  background: var(--foreground);
}

.current-time {
  opacity: 0;
  transition:
    opacity 200ms ease,
    color 200ms ease;
}

.duration__frame:hover .current-time {
  opacity: 1;
  color: var(--foreground-muted);
}
</style>
