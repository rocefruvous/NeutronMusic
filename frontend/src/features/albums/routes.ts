export const albumRoutes = [
  {
    path: "/album/:id",
    name: "album",
    component: () => import("./pages/AlbumPage.vue"),
  },
];
