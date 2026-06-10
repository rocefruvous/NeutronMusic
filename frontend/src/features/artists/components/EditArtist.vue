<script setup lang="ts">
import { reactive } from "vue";
import { useFormBuilder } from "@/shared/composables/UseFormBuilder";
import { useFileField } from "@/shared/composables/UseFileField";

import { updateArtist } from "@/features/artists/api";

import { editArtistModal } from "../state";

const props = defineProps({
  public_id: String,
});

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
  await updateArtist(props.public_id, data);
};
</script>

<template>
  <div
    @click="editArtistModal.open = false"
    v-if="editArtistModal.open"
    class="create-menu__outer fixed inset-0 flex items-center justify-center"
  >
    <div @click.stop class="create-menu flex flex-col p-5">
      <span class="primary-title--secondary text-center mb-6">
        <h2>Edit artist</h2>
      </span>

      <form class="artist__form flex flex-col gap-1.5" @submit.prevent="handleSubmit">
        <div class="form__full-field">
          <label>Name</label>
          <input class="form__input" type="text" v-model="form.name" />
        </div>
        <div class="form__full-field">
          <label>Profile Picture</label>
          <input class="form__file" type="file" @change="profileFile.onChange" />
        </div>
        <div class="form__full-field">
          <label>Cover Picture</label>
          <input class="form__file" type="file" @change="coverFile.onChange" />
        </div>
        <div class="form__full-field">
          <label>Bio</label>
          <textarea class="form__input" type="text" v-model="form.bio" placeholder="bio" />
        </div>

        <div class="flex flex-row justify-between gap-1.5 mt-1.5">
          <button
            @click="editArtistModal.open = false"
            class="form__submit button--secondary w-1/2"
            type="button"
          >
            Cancel
          </button>
          <button class="form__submit button--main w-1/2" type="submit">Save</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped></style>
