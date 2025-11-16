<template>
  <div class="admin-layout">
    <aside class="sidebar" v-if="isAuthenticated">
      <div class="sidebar-header">
        <h2>管理后台</h2>
        <p>{{ username }}</p>
      </div>
      <nav class="sidebar-nav">
        <router-link to="/admin" class="nav-item" exact>
          <span class="icon">📊</span>
          <span>仪表盘</span>
        </router-link>
        <router-link to="/admin/blogs" class="nav-item">
          <span class="icon">📝</span>
          <span>博客管理</span>
        </router-link>
        <router-link to="/admin/services" class="nav-item">
          <span class="icon">🔗</span>
          <span>服务管理</span>
        </router-link>
        <router-link to="/admin/events" class="nav-item">
          <span class="icon">📅</span>
          <span>活动管理</span>
        </router-link>
        <router-link to="/admin/settings" class="nav-item">
          <span class="icon">⚙️</span>
          <span>系统设置</span>
        </router-link>
        <a href="#" @click.prevent="logout" class="nav-item logout">
          <span class="icon">🚪</span>
          <span>退出登录</span>
        </a>
      </nav>
    </aside>
    <main class="main-content">
      <router-view></router-view>
    </main>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const isAuthenticated = computed(() => {
  return !!localStorage.getItem('admin_token')
})

const username = computed(() => {
  const admin = localStorage.getItem('admin_user')
  return admin ? JSON.parse(admin).username : ''
})

const logout = () => {
  localStorage.removeItem('admin_token')
  localStorage.removeItem('admin_user')
  router.push('/admin/login')
}
</script>

<style scoped>
.admin-layout {
  display: flex;
  min-height: 100vh;
  background: #f5f5f5;
}

.sidebar {
  width: 250px;
  background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
  color: white;
  padding: 2rem 0;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
}

.sidebar-header {
  padding: 0 1.5rem;
  margin-bottom: 2rem;
}

.sidebar-header h2 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.sidebar-header p {
  opacity: 0.9;
  font-size: 0.9rem;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 1rem 1.5rem;
  color: white;
  text-decoration: none;
  transition: all 0.3s;
  border-left: 3px solid transparent;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.1);
  border-left-color: white;
}

.nav-item.router-link-active {
  background: rgba(255, 255, 255, 0.2);
  border-left-color: white;
}

.nav-item .icon {
  margin-right: 0.75rem;
  font-size: 1.2rem;
}

.nav-item.logout {
  margin-top: auto;
  opacity: 0.8;
}

.main-content {
  flex: 1;
  padding: 2rem;
  overflow-y: auto;
}
</style>
