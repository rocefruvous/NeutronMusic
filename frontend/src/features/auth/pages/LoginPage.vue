<script setup lang="ts">
import { reactive } from "vue";
import { login } from "../api";

const form = reactive({
  username: "",
  password: "",
});

const handleSubmit = async () => {
  await login(form);
};
</script>

<template>
  <form id="login-form" @submit.prevent="handleSubmit">
    <span class="primary-title--secondary text-center mb-6"> Welcome back! </span>
    <div class="form__full-field">
      <label>Username</label>
      <input class="form__input" type="text" v-model="form.username" />
    </div>
    <div class="form__full-field">
      <label>Password</label>
      <input class="form__input" type="password" v-model="form.password" />
    </div>
    <button class="form__submit w-full" type="submit">Log in</button>
    <div class="form__sub-text">
      New user? <router-link to="/auth/register">Sign up</router-link>
    </div>
  </form>
</template>

<style scoped></style>
