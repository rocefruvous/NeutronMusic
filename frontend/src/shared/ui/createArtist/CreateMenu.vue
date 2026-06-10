<script setup lang="ts">
import { reactive } from "vue";
import { useRouter } from "vue-router";
import { useFormBuilder } from "@/shared/composables/UseFormBuilder";

import { createArtist } from "@/features/artists/api";

import { artistCreateModal } from "./state";

const router = useRouter();

const form = reactive({
  name: "",
});

const { toFormData } = useFormBuilder();

const handleSubmit = async () => {
  const data = toFormData(form);
  const createData = await createArtist(data);

  router.push({
    name: "artist",
    params: {
      public_id: createData?.public_id,
    },
  });
  artistCreateModal.open = false;
};
</script>

<template>
  <div
    @click="artistCreateModal.open = false"
    v-if="artistCreateModal.open"
    class="create-menu__outer fixed inset-0 flex items-center justify-center"
  >
    <div @click.stop class="create-menu flex flex-col p-5">
      <span class="primary-title--secondary text-center mb-6">
        <h2>Create a new artist</h2>
      </span>

      <form class="artist__form flex flex-col gap-1.5" @submit.prevent="handleSubmit">
        <div class="form__full-field">
          <label>Name</label>
          <input class="form__input" type="text" v-model="form.name" />
        </div>

        <div class="flex flex-row justify-between gap-1.5 mt-1.5">
          <button
            @click="artistCreateModal.open = false"
            class="form__submit button--secondary w-1/2"
            type="button"
          >
            Cancel
          </button>

          <button class="form__submit w-1/2" type="submit">Create</button>
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
