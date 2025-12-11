import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import Painters from '@/components/AppPainters.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    redirect: '/painters',
  },
  {
    path: '/painters',
    name: 'Painters',
    component: Painters,
    props: (route) => {
      return route.query
    },
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
