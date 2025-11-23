import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import UFMGLayout from "@/layouts/UFMGLayout.vue";
import UFMG from "./views/UFMG.vue";
import Plano from "./views/UFMG/Plano.vue";
import PlanoSidebar from "./views/UFMG/PlanoSidebar.vue";
import Material from "./views/UFMG/Material.vue";
import MaterialSidebar from "./views/UFMG/MaterialSidebar.vue";
import ClassView from "./views/UFMG/ClassView.vue";

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
            sidebar: PlanoSidebar,
          },
        },
        {
          path: "material",
          name: "Material",
          components: {
            default: Material,
            sidebar: MaterialSidebar,
          },
        },
        {
          path: "classes/:code",
          name: "Class",
          component: ClassView,
        },
      ],
    },
  ],
});
