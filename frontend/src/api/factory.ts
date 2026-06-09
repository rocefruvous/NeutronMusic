import { request } from "./request";

export const apiClient = {
  get: <T>(url: string) => request<T>("get", url),
  post: <T>(url: string, data?: unknown) => request<T>("post", url, data),
  patch: <T>(url: string, data?: unknown) => request<T>("patch", url, data),
  put: <T>(url: string, data?: unknown) => request<T>("put", url, data),
  delete: <T>(url: string) => request<T>("delete", url),
};
