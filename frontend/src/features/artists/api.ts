import { API_BASE, api } from "@/api/client";
import { endpoints } from "@/api/endpoints";
import { apiClient } from "@/api/factory";

export const artistMedia = {
  cover: (id: string) => `${API_BASE}/artists/${id}/cover-image/`,
  profile: (id: string) => `${API_BASE}/artists/${id}/profile-image/`,
};

export async function getArtist(id: string) {
  const data = await api.get(endpoints.artists.detail + id);
  return data;
}

export async function createArtist(data: FormData) {
  const res = apiClient.post(endpoints.artists.detail, data);
  return res;
}
