import {createRouter, createWebHistory} from 'vue-router'
import LoginView from '@/components/LoginView.vue';
import HomeView from '@/components/HomeView.vue';

// Vue.use(Router);
const routes = [
    {
        path: '/login',
        name: 'LoginView',
        component: LoginView
    },
    {
        path: '/home',
        name: 'HomeView',
        component: HomeView,
        meta: {requiresAuth: true}
    }
]

// 创建路由器实例
const router = createRouter({
    history: createWebHistory(),
    routes
})

// 路由守卫，检查token
router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('token');
    if (to.matched.some(record => record.meta.requiresAuth) && !token) {
        next('/login');
    } else {
        next();
    }
})

// 导出全局注册
export default router