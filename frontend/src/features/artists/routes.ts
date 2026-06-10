export const artistRoutes = [
  {
    path: "/artist/:public_id",
    name: "artist",
    component: () => import("./pages/ArtistPage.vue"),
    redirect: { name: "artist-songs" },
    children: [
      {
        path: "",
        name: "artist-songs",
        component: () => import("./pages/SongsPage.vue"),
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
