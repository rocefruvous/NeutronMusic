<script setup lang="ts">
import { computed, ref, watchEffect } from "vue";
import { useRoute } from "vue-router";
import { profileMedia, getProfile } from "../api";

import IdentityCard from "@/shared/components/IdentityCard.vue";

const route = useRoute();
const data = ref<any>(null);

const public_id = computed(() => route.params.username as string);

const urls = computed(() => ({
  profile: profileMedia.profile(public_id.value),
}));

async function fetchProfile(id: string) {
  const { data: res } = await getProfile(id);
  data.value = res;
}

watchEffect(() => {
  if (public_id.value) fetchProfile(public_id.value);
});
</script>

<template>
  <div class="profile__banner h-96"></div>
  <div class="flex justify-center">
    <div class="flex flex-row section w-full">
      <div class="pr-12 pl-12 w-96">
        <IdentityCard :name="data?.username" :src="urls.profile" />
        <p class="text-secondary">{{ data?.bio }}</p>
      </div>
      <div>
        <div>
          <ul class="tabs flex flex-row"></ul>
        </div>
        <router-view />
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile__frame {
  margin-top: 4rem;
  display: flex;
}
.profile__image {
  width: var(--avatar-lg);
  border-radius: 1rem;
}
.profile__label {
  margin: 0;
}
</style>
