<script setup lang="ts">
import AppHeader from "@/core/header/AppHeader.vue";
import AppPlayer from "@/core/audio/player/AppPlayer.vue";
import CreateMenu from "@/shared/ui/createArtist/CreateMenu.vue";
</script>

<template>
  <AppHeader />
  <router-view />
  <AppPlayer />
  <CreateMenu />
</template>

<style scoped></style>
