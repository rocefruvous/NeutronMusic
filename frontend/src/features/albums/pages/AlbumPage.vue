<script setup lang="ts">
import { computed, ref, watchEffect } from "vue";
import { useRoute } from "vue-router";
import { albumMedia, getAlbum } from "../api";

import { Pencil, Plus } from "@lucide/vue";

import IdentityCard from "@/shared/components/IdentityCard.vue";

import CreateSong from "../components/CreateSong.vue";
import SongsPage from "../components/SongsPage.vue";

import { getArtist } from "@/features/artists/api";

import { songCreateModal } from "../state";

const route = useRoute();
const data = ref<any>(null);
const artistData = ref<any>(null);

const albumId = computed(() => route.params.id as string);

const urls = computed(() => ({
  cover: albumMedia.cover(albumId.value),
}));

async function fetchArtist(id: string) {
  const { data: res } = await getArtist(id);
  artistData.value = res;
}

async function fetchAlbum(id: string) {
  const { data: res } = await getAlbum(id);
  data.value = res;
  fetchArtist(res.artist);
}

const refreshAlbum = () => {
  fetchAlbum(albumId.value);
};

watchEffect(() => {
  if (albumId.value) fetchAlbum(albumId.value);
});
</script>

<template>
  <div
    class="profile__banner blur-xl h-96"
    :style="{
      backgroundImage: `linear-gradient(rgba(0,0,0, 0.2), var(--background)), url(${urls.cover})`,
    }"
  ></div>
  <div class="flex justify-center">
    <div class="flex flex-row section w-full">
      <div class="pr-12 pl-12 w-96">
        <IdentityCard :name="data?.name" :src="urls.cover" shape="square" />
        <div class="flex flex-row gap-1.5 mt-3 mb-6">
          <button
            @click="songCreateModal.open = true"
            class="button--main text-button artist__follow-button gap-1.5"
          >
            <Plus :size="18" />Create
          </button>
          <button class="button--main text-button artist__follow-button">
            <Pencil :size="18" />
          </button>
        </div>
        <p class="primary-title--secondary text-secondary">{{ artistData?.name }}</p>
        <p class="text-secondary">{{ artistData?.bio }}</p>
      </div>
      <div>
        <div>
          <ul class="tabs flex flex-row"></ul>
        </div>
        <SongsPage :id="albumId" />
        <router-view />
      </div>
    </div>
  </div>
  <CreateSong @created="refreshAlbum" :public_id="albumId" />
</template>

<style scoped>
.artist__follow-button {
  height: 2.25rem;
  border-radius: 100rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

.tabs__tab {
  display: flex;
  height: 100%;
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--foreground-muted);
  padding: 0.4rem 1.3rem;
  cursor: pointer;
  text-decoration: none;
}

.tabs__tab--active {
  color: var(--foreground);
  border-bottom: 2px solid var(--foreground);
}

.icon-button {
  padding: 0.8rem;
}

.text-button {
  padding: 0rem 2rem;
}
</style>
