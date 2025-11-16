import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'
import App from './App.vue'

// 导入页面组件
import Home from './views/Home.vue'
import Services from './views/Services.vue'
import Blog from './views/Blog.vue'
import BlogPost from './views/BlogPost.vue'
import Events from './views/Events.vue'
import About from './views/About.vue'

// 导入管理后台组件
import AdminLogin from './views/admin/Login.vue'
import AdminLayout from './views/admin/AdminLayout.vue'
import Dashboard from './views/admin/Dashboard.vue'
import BlogManage from './views/admin/BlogManage.vue'
import BlogEditor from './views/admin/BlogEditor.vue'

// 路由守卫
const requireAuth = (_to: any, _from: any, next: any) => {
  const token = localStorage.getItem('admin_token')
  if (!token) {
    next('/admin/login')
  } else {
    next()
  }
}

// 配置路由
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/services', name: 'Services', component: Services },
    { path: '/blog', name: 'Blog', component: Blog },
    { path: '/blog/:id', name: 'BlogPost', component: BlogPost },
    { path: '/events', name: 'Events', component: Events },
    { path: '/about', name: 'About', component: About },
    
    // 管理后台路由
    { path: '/admin/login', name: 'AdminLogin', component: AdminLogin },
    {
      path: '/admin',
      component: AdminLayout,
      beforeEnter: requireAuth,
      children: [
        { path: '', name: 'Dashboard', component: Dashboard },
        { path: 'blogs', name: 'BlogManage', component: BlogManage },
        { path: 'blogs/new', name: 'BlogNew', component: BlogEditor },
        { path: 'blogs/edit/:id', name: 'BlogEdit', component: BlogEditor },
        // 简化版本：服务和活动管理使用相同的管理界面模式
        { path: 'services', name: 'ServiceManage', component: BlogManage },
        { path: 'events', name: 'EventManage', component: BlogManage },
        { path: 'settings', name: 'Settings', component: Dashboard }
      ]
    }
  ],
  scrollBehavior(_to, _from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

const app = createApp(App)
app.use(router)
app.mount('#app')
