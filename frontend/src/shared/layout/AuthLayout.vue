<script setup lang="ts"></script>

<template>
  <div class="auth__main-frame absolute flex justify-center items-center w-full h-screen">
    <div class="auth__frame p-5 w-96">
      <router-view />
    </div>
  </div>
</template>

<style scoped>
.auth__main-frame {
  background-image: url(/src/assets/images/auth_background.png);
  background-position: center;
  background-size: cover;
}

.auth__frame {
  background: var(--background);
  border-radius: 1rem;
}
</style>
