import { userRoutes } from "@/features/users/routes";
import { searchRoutes } from "@/features/search/routes";
import { artistRoutes } from "@/features/artists/routes";
import { authRoutes } from "@/features/auth/routes";
import { albumRoutes } from "@/features/albums/routes";
import { browseRoutes } from "@/features/browse/routes";

import DefaultLayout from "@/shared/layout/DefaultLayout.vue";
import AuthLayout from "@/shared/layout/AuthLayout.vue";

export const routes = [
  {
    path: "/auth",
    component: AuthLayout,
    children: [...authRoutes],
  },
  {
    path: "/",
    component: DefaultLayout,
    children: [...browseRoutes, ...userRoutes, ...albumRoutes, ...searchRoutes, ...artistRoutes],
  },
];
