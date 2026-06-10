<script setup lang="ts">
import { computed, ref, watchEffect } from "vue";
import { useRoute } from "vue-router";
import { artistMedia, getArtist } from "../api";

import { Pencil, Plus } from "@lucide/vue";

import { albumCreateAlbum, editArtistModal } from "../state";

import IdentityCard from "@/shared/components/IdentityCard.vue";

import CreateAlbum from "../components/CreateAlbum.vue";
import EditArtist from "../components/EditArtist.vue";

const route = useRoute();
const data = ref<any>(null);

const public_id = computed(() => route.params.public_id as string);

const urls = computed(() => ({
  cover: artistMedia.cover(public_id.value),
  profile: artistMedia.profile(public_id.value),
}));

async function fetchArtist(id: string) {
  const { data: res } = await getArtist(id);
  data.value = res;
}

watchEffect(() => {
  if (public_id.value) fetchArtist(public_id.value);
});
</script>

<template>
  <div
    class="profile__banner h-96"
    :style="{
      backgroundImage: `linear-gradient(rgba(0,0,0, 0.2), var(--background)), url(${urls.cover})`,
    }"
  ></div>
  <div class="flex justify-center">
    <div class="flex flex-row section w-full">
      <div class="pr-12 pl-12 w-96">
        <IdentityCard :name="data?.name" :src="urls.profile" />
        <div class="flex flex-row gap-1.5 mt-3 mb-6">
          <button
            @click="albumCreateAlbum.open = true"
            class="button--main text-button artist__follow-button gap-1.5"
          >
            <Plus :size="18" />Create
          </button>
          <button
            @click="editArtistModal.open = true"
            class="button--main text-button artist__follow-button"
          >
            <Pencil :size="18" />
          </button>
        </div>
        <p class="text-secondary">{{ data?.bio }}</p>
      </div>
      <div class="w-1/2">
        <div>
          <ul class="tabs flex flex-row">
            <li>
              <RouterLink
                class="tabs__tab"
                active-class="tabs__tab--active"
                exact-active-class="tabs__tab--active"
                :to="{ name: 'artist-songs', params: { id: public_id } }"
              >
                Songs
              </RouterLink>
            </li>
            <li>
              <RouterLink
                class="tabs__tab"
                active-class="tabs__tab--active"
                exact-active-class="tabs__tab--active"
                :to="{ name: 'artist-albums', params: { id: public_id } }"
              >
                Albums
              </RouterLink>
            </li>
            <RouterLink
              class="tabs__tab"
              active-class="tabs__tab--active"
              exact-active-class="tabs__tab--active"
              :to="{ name: 'artist-liked', params: { id: public_id } }"
            >
              Liked
            </RouterLink>
          </ul>
        </div>
        <router-view />
      </div>
    </div>
  </div>
  <EditArtist :public_id="public_id" />
  <CreateAlbum :public_id="public_id" />
</template>

<style scoped>
.artist__follow-button {
  height: 2.25rem;
  border-radius: 999rem;
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
