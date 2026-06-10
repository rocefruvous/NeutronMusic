<script setup lang="ts">
import { reactive } from "vue";
import { useFormBuilder } from "@/shared/composables/UseFormBuilder";
import { useFileField } from "@/shared/composables/UseFileField";

import { createSong } from "@/features/songs/api";

import { songCreateModal } from "../state";

const emit = defineEmits<{
  (e: "created"): void;
}>();

const props = defineProps({
  public_id: String,
});

const form = reactive({
  name: "",
  album: props.public_id,
  track_number: "",
  explicit: null,
  audio: null,
});

const { toFormData } = useFormBuilder();

const audioFile = useFileField(form, "audio");

const handleSubmit = async () => {
  const data = toFormData(form);
  const res = await createSong(data);

  if (res) {
    console.log("emitting created");
    emit("created");
  }
};
</script>

<template>
  <div
    @click="songCreateModal.open = false"
    v-if="songCreateModal.open"
    class="create-menu__outer fixed inset-0 flex items-center justify-center"
  >
    <div @click.stop class="create-menu flex flex-col p-5">
      <span class="primary-title--secondary text-center mb-6">
        <h2>Create new song</h2>
      </span>

      <form class="artist__form flex flex-col gap-1.5" @submit.prevent="handleSubmit">
        <div class="form__full-field">
          <label>Name</label>
          <input class="form__input" type="text" v-model="form.name" />
        </div>
        <div class="form__full-field">
          <label>Song</label>
          <input class="form__file" type="file" @change="audioFile.onChange" />
        </div>
        <div class="form__full-field">
          <label>Track Number</label>
          <input class="form__input" type="number" v-model="form.track_number" />
        </div>
        <div class="form__full-field">
          <label>Explicit</label>
          <input class="form__boolean" type="checkbox" v-model="form.explicit" value="false" />
        </div>

        <div class="flex flex-row justify-between gap-1.5 mt-1.5">
          <button
            @click="songCreateModal.open = false"
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
