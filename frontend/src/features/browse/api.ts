import { API_BASE, api } from "@/api/client";
import { endpoints } from "@/api/endpoints";
import { apiClient } from "@/api/factory";

export async function getRecommendations(id: string) {
  const data = await api.get(endpoints.browse.list);
  return data;
}
