import { API_BASE, api } from "@/api/client";
import { endpoints } from "@/api/endpoints";

export async function search(query: string) {
  const data = await api.get(endpoints.search.query, {
    params: { q: query },
  });
  return data;
}
