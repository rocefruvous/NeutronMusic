<script setup lang="ts">
import { reactive } from "vue";
import { useFormBuilder } from "@/shared/composables/UseFormBuilder";
import { useFileField } from "@/shared/composables/UseFileField";

import { createArtist } from "@/features/artists/api";

import { artistCreateModal } from "./state";

const form = reactive({
  name: "",
  profile_image: null,
  cover_image: null,
  bio: "",
});

const { toFormData } = useFormBuilder();

const profileFile = useFileField(form, "profile_image");
const coverFile = useFileField(form, "cover_image");

const handleSubmit = async () => {
  const data = toFormData(form);
  await createArtist(data);
};
</script>

<template>
  <div
    @click="artistCreateModal.open = false"
    v-if="artistCreateModal.open"
    class="create-menu__outer fixed inset-0 flex items-center justify-center"
  >
    <div @click.stop class="create-menu flex flex-col p-5">
      <div class="flex flex-row justify-between">
        <h2>Create new artist</h2>
        <button>X</button>
      </div>
      <form class="artist__form flex flex-col gap-1.5" @submit.prevent="handleSubmit">
        <label>Name</label>
        <input class="form__input" type="text" v-model="form.name" placeholder="name" />
        <label>Profile Picture</label>
        <input class="form__file" type="file" @change="profileFile.onChange" />
        <label>Cover Picture</label>
        <input class="form__file" type="file" @change="coverFile.onChange" />
        <label>Bio</label>
        <textarea class="form__input" type="text" v-model="form.bio" placeholder="bio" />
        <div class="flex flex-row justify-between gap-1.5 mt-1.5">
          <button @click="artistCreateModal.open = false" class="form__submit w-1/2" type="button">
            Cancel
          </button>
          <button class="form__submit w-1/2" type="submit">Save</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.create-menu__outer {
  background-color: #00000093;
}

.create-menu {
  background-color: var(--background);
  border-radius: 1em;
}
</style>
