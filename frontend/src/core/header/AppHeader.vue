<script setup lang="ts">
import ProfileMenu from "./ProfileMenu.vue";
import { useAuth } from "@/features/auth/composables/UseAuth";

import { ref } from "vue";
import { useRouter } from "vue-router";
import { House, Search, Plus } from "@lucide/vue";

import { artistCreateModal } from "@/shared/ui/createArtist/state";

const router = useRouter();

const { isLoggedIn } = useAuth();

const query = ref("");

function goSearch() {
  const val = query.value.trim();
  if (!val) return;

  router.push({ name: "search", query: { q: val } });
}
</script>

<template>
  <header class="fixed w-full top-0 z-50 px-2.5">
    <nav class="flex justify-between h-full m-auto items-center">
      <router-link to="/" class="header__button header__button--text"><House /></router-link>
      <div class="header__button header__button--text mr-auto ml-2.5 gap-2">
        <Search :size="20" />
        <input v-model="query" @keyup.enter="goSearch" type="text" placeholder="Search" />
      </div>

      <span v-if="isLoggedIn == true" class="flex flex-row gap-2.5">
        <a @click="artistCreateModal.open = true" class="header__button header__button--icon">
          <Plus />
        </a>
        <ProfileMenu />
      </span>
      <span v-else-if="!isLoggedIn">
        <router-link to="/auth/login" class="header__button--sign-up button--main"
          >Sign In</router-link
        >
      </span>
    </nav>
  </header>
</template>

<style scoped>
header {
  color: white;
  background-color: transparent;
  height: 53px;
}

header nav {
  max-width: 1656px;
}

.header__button {
  height: 2.25rem;
  background-color: rgba(255, 255, 255, 0.15);
  color: inherit;
  backdrop-filter: blur(0.5rem);
  border-radius: 100rem;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.header__button--text {
  padding: 0rem 0.875rem;
}

.header__button--icon {
  padding: 0.3rem;
}

.header__button--sign-up {
  height: 2.25rem;
  padding: 0rem 0.875rem;
  border-radius: 100rem;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.header__links li {
  list-style-type: none;
}

.header-link {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
}

.header-link__dot {
  height: 0.5em;
  width: 0.5em;
  margin-top: 0.2em;
  border-radius: 100%;
}

.header-link:hover .header-link__dot {
  background-color: white;
}

.search-box {
  margin-left: 1em;
  margin-right: auto;
}

.search-box input {
  background: var(--surface);
  color: var(--foreground);
  border-radius: 0.3rem;
  border: none;
  padding: 0.6em;
}
</style>
