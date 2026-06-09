<script setup lang="ts">
import { reactive } from "vue";
import { register } from "../api";

const form = reactive({
  username: "",
  email: "",
  password: "",
  password2: "",
});

const handleSubmit = async () => {
  await register(form);
};
</script>

<template>
  <form class="flex flex-col" @submit.prevent="handleSubmit">
    <span class="primary-title--secondary text-center mb-6"> Create an account </span>
    <div class="form__full-field">
      <label>Username</label>
      <input class="form__input" type="text" v-model="form.username" />
    </div>
    <div class="form__full-field">
      <label>Email</label>
      <input class="form__input" type="email" v-model="form.email" />
    </div>
    <div class="form__full-field">
      <label>Password</label>
      <input class="form__input" type="password" v-model="form.password" />
    </div>
    <div class="form__full-field">
      <label>Repeat the password</label>
      <input class="form__input" type="password" v-model="form.password2" />
    </div>

    <button class="form__submit" type="submit">Sign up</button>
    <div class="form__sub-text">
      Already have an account? <router-link to="/auth/login">Log in</router-link>
    </div>
  </form>
</template>

<style scoped></style>
