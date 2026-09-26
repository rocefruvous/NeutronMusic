import axios from "axios";

export const API_BASE = "/api";

export const api = axios.create({
  baseURL: API_BASE,
  withCredentials: true,
  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFToken",
});
