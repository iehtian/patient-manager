import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import patients from '@/components/AppPatient.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    redirect: '/patients',
  },
  {
    path: '/patients',
    name: 'patients',
    component: patients,
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
