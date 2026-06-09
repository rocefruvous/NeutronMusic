export const authRoutes = [
  { path: "register", name: "register", component: () => import("./pages/RegisterPage.vue") },
  { path: "login", name: "login", component: () => import("./pages/LoginPage.vue") },
];
