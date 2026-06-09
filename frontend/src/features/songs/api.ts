import { API_BASE, api } from "@/api/client";
import { endpoints } from "@/api/endpoints";
import { apiClient } from "@/api/factory";

import { audioState } from "@/core/audio/player/state";

export async function getSongs(id: string) {
  const data = await api.get(endpoints.songs.list, {
    params: { album: id },
  });
  return data;
}

export async function getSong(id: string) {
  const res = await api.get(endpoints.songs.list + id);
  return res.data;
}

export async function createSong(data: FormData) {
  apiClient.post(endpoints.songs.list, data);
}

export async function playSong(id: string) {
  audioState.songId = id;
}
