<script setup lang="ts">
import { reactive, ref } from "vue";
import { useFormBuilder } from "@/shared/composables/UseFormBuilder";
import { useFileField } from "@/shared/composables/UseFileField";

import { createSong } from "@/features/songs/api";

const emit = defineEmits<{
  (e: "created"): void;
}>();

const props = defineProps({
  public_id: String,
});

const show_menu = ref(false);

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
  <button @click="show_menu = !show_menu">Create Album test</button>

  <div
    @click="show_menu = !show_menu"
    v-if="show_menu"
    class="create-menu__outer fixed inset-0 flex items-center justify-center"
  >
    <div @click.stop class="create-menu flex flex-col p-5">
      <div class="flex flex-row justify-between">
        <h2>Create new song</h2>
        <button>X</button>
      </div>
      <form class="artist__form flex flex-col gap-1.5" @submit.prevent="handleSubmit">
        <label>Name</label>
        <input class="form__input" type="text" v-model="form.name" placeholder="Name the song" />
        <label>Song</label>
        <input class="form__file" type="file" @change="audioFile.onChange" />
        <label>Track Number</label>
        <input class="form__input" type="number" v-model="form.track_number" placeholder="1" />
        <label>Explicit</label>
        <input class="form__input" type="checkbox" v-model="form.explicit" value="false" />
        <div class="flex flex-row justify-between gap-1.5 mt-1.5">
          <button
            @click="show_menu = !show_menu"
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

<style scoped>
.create-menu__outer {
  background-color: #00000093;
}

.create-menu {
  background-color: var(--background);
  border-radius: 1em;
}
</style>
