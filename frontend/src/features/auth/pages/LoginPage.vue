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
  <div class="login__main-frame">
    <h1>Login!!</h1>
    <form id="login-form" @submit.prevent="handleSubmit">
      <label>Username</label>
      <input class="form__input" type="text" v-model="form.username" placeholder="username" />
      <p></p>
      <label>Password</label>
      <input class="form__input" type="password" v-model="form.password" placeholder="password" />
      <p></p>
      <button class="form__submit" type="submit">Log in</button>
      <div>New user? <router-link to="/auth/register">Sign up</router-link></div>
    </form>
  </div>
  <P></P>
</template>

<style scoped>
.login__main-frame {
  padding-bottom: 25%;
  background-size: cover;
  background-image: url(https://cdn.discordapp.com/attachments/635625973764849684/1506584475708948593/wallhaven-k82231.png?ex=6a12c021&is=6a116ea1&hm=d809216634e59dbec1c3f3f4237eebd3ebdc63c8885873bedaeb61fc211eb085);
}

#login-form {
  display: flex;
  flex-direction: column;
  width: 30rem;
  margin: auto;
  background-color: var(--background);
  padding: 1rem;
  border-radius: 0.3rem;
  margin-top: 15%;
}
</style>
