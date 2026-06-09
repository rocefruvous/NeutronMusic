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
  <div class="login__main-frame">
    <h1>Login!!</h1>
    <form id="login-form" @submit.prevent="handleSubmit">
      <label>Username</label>
      <input class="form__input" type="text" v-model="form.username" placeholder="username" />
      <p></p>
      <label>Email</label>
      <input class="form__input" type="email" v-model="form.email" placeholder="email" />
      <label>Password</label>
      <input class="form__input" type="password" v-model="form.password" placeholder="password" />
      <label>Repeat the password</label>
      <input class="form__input" type="password" v-model="form.password2" placeholder="password" />
      <p></p>
      <button class="form__submit" type="submit">Sign up</button>
      <div>New user? <router-link to="/register">Sign up</router-link></div>
    </form>
  </div>
  <P></P>
</template>

<style scoped></style>
