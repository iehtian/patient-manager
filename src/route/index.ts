import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import patient_show from '@/view/AppPatient.vue'


const routes: RouteRecordRaw[] = [
  {
    path: '/patients',
    name: 'patients',
    component: patient_show,
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
