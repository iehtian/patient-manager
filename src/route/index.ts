import { createRouter, createWebHistory } from 'vue-router'
import AppShowPaint from '@/components/AppShowPainter.vue'

const routes = [
  {
    path: '/ShowPainter',
    name: 'ShowPainter',
    component: AppShowPaint,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
