import { API_BASE, api } from "@/api/client";
import { endpoints } from "@/api/endpoints";
import { apiClient } from "@/api/factory";

export const albumMedia = {
  cover: (id: string) => `${API_BASE}/albums/${id}/cover-image/`,
};

export async function getAlbums(id: string) {
  const data = await api.get(endpoints.albums.list, {
    params: { artist: id },
  });
  return data;
}

export async function getAlbum(id: string) {
  const res = await api.get(endpoints.albums.list + id);
  return res;
}

export async function createAlbum(data: FormData) {
  apiClient.post(endpoints.albums.list, data);
}
