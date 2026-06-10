<script setup lang="ts">
import { reactive, ref } from "vue";
import { useFormBuilder } from "@/shared/composables/UseFormBuilder";
import { useFileField } from "@/shared/composables/UseFileField";

import { createAlbum } from "@/features/albums/api";

import { albumCreateAlbum } from "../state";

const props = defineProps({
  public_id: String,
});

const form = reactive({
  name: "",
  artist: props.public_id,
  cover_art: null,
  release_date: "",
});

const { toFormData } = useFormBuilder();

const coverFile = useFileField(form, "cover_art");

const handleSubmit = async () => {
  const data = toFormData(form);
  await createAlbum(data);
};
</script>

<template>
  <div
    @click="albumCreateAlbum.open = false"
    v-if="albumCreateAlbum.open"
    class="create-menu__outer fixed inset-0 flex items-center justify-center"
  >
    <div @click.stop class="create-menu flex flex-col p-5">
      <span class="primary-title--secondary text-center mb-6">
        <h2>Create new album</h2>
      </span>
      <form class="artist__form flex flex-col gap-1.5" @submit.prevent="handleSubmit">
        <div class="form__full-field">
          <label>Name</label>
          <input class="form__input" type="text" v-model="form.name" placeholder="Name the album" />
        </div>
        <div class="form__full-field">
          <label>Cover Art</label>
          <input class="form__file" type="file" @change="coverFile.onChange" />
        </div>
        <div class="form__full-field">
          <label>Release Date</label>
          <input class="form__input" type="date" v-model="form.release_date" placeholder="bio" />
        </div>
        <div class="flex flex-row justify-between gap-1.5 mt-1.5">
          <button
            @click="albumCreateAlbum.open = false"
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
