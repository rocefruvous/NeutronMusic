import { api } from "@/api/client";
import { getCookie } from "./cookies";

export async function request<T>(
  method: "get" | "post" | "patch" | "put" | "delete",
  url: string,
  data?: any,
): Promise<T | null> {
  const csrfToken = getCookie("csrftoken");

  try {
    const res = await api.request<T>({
      method,
      url,
      data,
      headers: {
        "X-CSRFToken": csrfToken || "",
      },
    });

    return res.data;
  } catch (err: any) {
    const status = err?.response?.status;
    const data = err?.response?.data;

    if (status === 400) {
      console.log("bad request:", data?.error);
      return null;
    }

    console.log("request failed:", err);
    return null;
  }
}
