import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import UFMGLayout from "@/layouts/UFMGLayout.vue";
import UFMG from "./views/UFMG.vue";
import Plano from "./views/UFMG/Plano.vue";
import UFMGSidebar from "./views/UFMG/UFMGSidebar.vue";

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/ufmg",
      name: "UFMG",
      component: UFMG,
    },
    {
      path: "/ufmg",
      component: UFMGLayout,
      children: [
        {
          path: "plano",
          name: "Plano",
          components: {
            default: Plano,
            sidebar: UFMGSidebar,
          },
        },
      ],
    },
  ],
});
