<script setup lang="ts">
import { useAuth } from "@/features/auth/composables/UseAuth";
import { ref } from "vue";

const { user } = useAuth();

const user_data = user.value;

const show_menu = ref(false);
</script>

<template>
  <div class="profile__container">
    <button @click="show_menu = !show_menu" class="profile__button">
      <img
        :src="`http://localhost:8000/api/user/${user_data?.username}/profile-image/`"
        class="profile__profile-image"
      />
    </button>
    <div class="relative">
      <div class="inline">
        <div v-if="show_menu" class="absolute right-0 mt-2 profile__menu backdrop-shadow p-6">
          <div class="">
            <ul class="dropdown-menu">
              <li>
                <router-link :to="{ name: 'profile', params: { username: user_data?.username } }"
                  >Profile</router-link
                >
              </li>
              <li><router-link to="/settings">Settings</router-link></li>
              <li>Log out</li>
            </ul>
          </div>
          <!-- <div class="z-10 fixed top-0 left-0 w-screen h-screen"></div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile__menu {
  background-color: var(--background);
  border-radius: 0.5rem;
}

.profile__button {
  display: inline;
  filter: drop-shadow(rgba(16, 18, 26, 0.15) 3px 3px 30px);
  background-color: transparent;
  color: var(--foreground);
  border: none;
  cursor: pointer;
}

.profile__button:hover .profile__profile-image {
  border: 2px solid var(--primary);
}

.profile__container {
  height: var(--avatar-sm);
}

.profile__profile-image {
  width: var(--avatar-sm);
  border-radius: 100vw;
  transition: 250ms;
}
</style>
