import { createRouter, createWebHistory } from 'vue-router'
import Painters from '@/components/AppPainters.vue'
const routes = [
  {
    path: '/painters',
    name: 'Painters',
    component: Painters,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
