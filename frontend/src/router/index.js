import { createRouter, createWebHistory } from "vue-router"

import Login from "../views/Login.vue"
import Register from "../views/Register.vue"
import Consultations from "../views/Consultations.vue"

const routes = [
  { path: "/", redirect: "/consultations" },

  { path: "/login", component: Login, meta: { guest: true } },
  { path: "/register", component: Register, meta: { guest: true } },

  {
    path: "/consultations",
    component: Consultations,
    meta: { requiresAuth: true },
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("access_token")

  // Not logged in & trying to access protected page
  if (to.meta.requiresAuth && !token) {
    return next("/login")
  }

  // Logged in & trying to access login/register
  if (to.meta.guest && token) {
    return next("/consultations")
  }

  next()
})

export default router
