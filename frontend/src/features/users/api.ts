import { API_BASE, api } from "@/api/client";
import { endpoints } from "@/api/endpoints";
import { apiClient } from "@/api/factory";

import { useAuth } from "@/features/auth/composables/UseAuth";

export const profileMedia = {
  profile: (username: string) => `${API_BASE}/user/${username}/profile-image/`,
};

export async function updateProfile(data: FormData) {
  const res = apiClient.patch(endpoints.auth.me, data);

  const { fetchMe } = useAuth();

  if (res != null) {
    fetchMe();
    return;
  }

  return res;
}

export async function getProfile(id: string) {
  const data = await api.get(endpoints.user.profile + id);
  return data;
}
