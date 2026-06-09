import { endpoints } from "@/api/endpoints";
import { apiClient } from "@/api/factory";

import { useAuth } from "./composables/UseAuth";

export async function login(data: FormData) {
  const res = apiClient.post(endpoints.auth.login, data);

  const { fetchMe } = useAuth();

  if (res != null) {
    fetchMe();
    return;
  }

  return res;
}

export async function register(data: FormData) {
  const res = apiClient.post(endpoints.auth.register, data);

  const { fetchMe } = useAuth();

  if (res != null) {
    fetchMe();
    return;
  }

  return res;
}
