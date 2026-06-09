import { computed } from "vue";
import { storeToRefs } from "pinia";
import { useAuthStore } from "../store";

export function useAuth() {
  const store = useAuthStore();
  const { user } = storeToRefs(store);

  return {
    user,
    isLoggedIn: computed(() => !!user.value),
    fetchMe: store.fetchMe,
    logout: store.logout,
  };
}
