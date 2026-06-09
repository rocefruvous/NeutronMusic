export const userRoutes = [
  {
    path: "/profile/:username",
    name: "profile",
    component: () => import("./pages/ProfilePage.vue"),
  },
  { path: "/settings", name: "settings", component: () => import("./pages/SettingsPage.vue") },
];
