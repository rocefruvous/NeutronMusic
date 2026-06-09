import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import { useAuth } from "@/features/auth/composables/UseAuth";

import "./assets/styles/variables.css";
import "./assets/styles/base.css";

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);

const { fetchMe } = useAuth();

await fetchMe();

app.mount("#app");
