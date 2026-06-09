import { defineStore } from "pinia";
import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api/",
  withCredentials: true,

  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFToken",
});

type User = {
  username: string | null;
};

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null as User | null,
    loaded: false,
  }),

  actions: {
    async fetchMe() {
      if (this.loaded) return this.user;

      try {
        const { data } = await api.get("/user/me");

        this.user = data;
        return data;
      } catch (err) {
        this.user = null;
        return null;
      } finally {
        this.loaded = true;
      }
    },

    logout() {
      this.user = null;
      this.loaded = false;
    },
  },
});
