export const artistRoutes = [
  {
    path: "/artist/:public_id",
    name: "artist",
    component: () => import("./pages/ArtistPage.vue"),
    children: [
      {
        path: "",
        name: "artist-songs",
        component: "",
      },
      {
        path: "albums",
        name: "artist-albums",
        component: () => import("./pages/AlbumsPage.vue"),
      },
      {
        path: "about",
        name: "artist-about",
        component: "",
      },
    ],
  },
];
