<script setup lang="ts">
import { computed, reactive } from "vue";
import { useAuth } from "@/features/auth/composables/UseAuth";
import { updateProfile, profileMedia } from "../api";

import { useFormBuilder } from "@/shared/composables/UseFormBuilder";
import { useFileField } from "@/shared/composables/UseFileField";

const { user, isLoggedIn } = useAuth();

const urls = computed(() => ({
  profile: profileMedia.profile(user.value?.username),
}));

const form = reactive({
  username: "",
  profile_image: null,
  bio: "",
});

const { toFormData } = useFormBuilder();

const profile_image = useFileField(form, "profile_image");

const handleSubmit = async () => {
  const data = toFormData(form);
  await updateProfile(data);
};
</script>

<template>
  <div class="profile-customisation">
    <div>
      <form class="profile-customisation__form" @submit.prevent="handleSubmit">
        <label>Username</label>
        <input class="form__input" type="text" v-model="form.username" placeholder="username" />
        <label>Profile Picture</label>
        <input class="form__file" type="file" @change="profile_image.onChange" />
        <label>Bio</label>
        <textarea class="form__input" type="text" v-model="form.bio" placeholder="bio" />
        <button class="form__submit" type="submit">Save</button>
      </form>
    </div>
    <div>
      <p>Profile Picture</p>
      <img :src="urls.profile" class="profile-image" />
    </div>
  </div>
</template>

<style scoped>
.profile-customisation {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.profile-customisation__form {
  display: flex;
  flex-direction: column;
  padding: 1em;
}

.profile-customisation__form input,
.profile-customisation__form textarea {
  margin-top: 0.3em;
  margin-bottom: 1em;
}

.profile-image {
  width: var(--avatar-lg);
  border-radius: 1rem;
}
</style>
