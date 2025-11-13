<template>
  <div class="dashboard">
    <h1>管理仪表盘</h1>
    
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon">📝</div>
        <div class="stat-content">
          <h3>{{ stats.blogs }}</h3>
          <p>博客文章</p>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">🔗</div>
        <div class="stat-content">
          <h3>{{ stats.services }}</h3>
          <p>服务链接</p>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">📅</div>
        <div class="stat-content">
          <h3>{{ stats.events }}</h3>
          <p>活动信息</p>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">👁️</div>
        <div class="stat-content">
          <h3>{{ stats.views }}</h3>
          <p>总访问量</p>
        </div>
      </div>
    </div>

    <div class="quick-actions">
      <h2>快捷操作</h2>
      <div class="actions-grid">
        <router-link to="/admin/blogs/new" class="action-card">
          <span class="action-icon">✍️</span>
          <span>创建新文章</span>
        </router-link>
        <router-link to="/admin/services/new" class="action-card">
          <span class="action-icon">➕</span>
          <span>添加服务</span>
        </router-link>
        <router-link to="/admin/events/new" class="action-card">
          <span class="action-icon">📆</span>
          <span>创建活动</span>
        </router-link>
        <router-link to="/" class="action-card">
          <span class="action-icon">🏠</span>
          <span>返回前台</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'

const stats = ref({
  blogs: 0,
  services: 0,
  events: 0,
  views: 1234 // 模拟数据
})

onMounted(async () => {
  try {
    const [blogsRes, servicesRes, eventsRes] = await Promise.all([
      fetch(`${API_BASE}/blogs?published=false`),
      fetch(`${API_BASE}/services?active=false`),
      fetch(`${API_BASE}/events?published=false`)
    ])

    const [blogs, services, events] = await Promise.all([
      blogsRes.json(),
      servicesRes.json(),
      eventsRes.json()
    ])

    stats.value.blogs = blogs.length
    stats.value.services = services.length
    stats.value.events = events.length
  } catch (error) {
    console.error('加载统计数据失败:', error)
  }
})
</script>

<style scoped>
.dashboard {
  max-width: 1200px;
}

h1 {
  font-size: 2rem;
  margin-bottom: 2rem;
  color: #333;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.stat-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  gap: 1.5rem;
  transition: transform 0.3s;
}

.stat-card:hover {
  transform: translateY(-5px);
}

.stat-icon {
  font-size: 3rem;
}

.stat-content h3 {
  font-size: 2rem;
  color: #06b6d4;
  margin-bottom: 0.25rem;
}

.stat-content p {
  color: #666;
  font-size: 0.9rem;
}

.quick-actions h2 {
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
  color: #333;
}

.actions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.action-card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
  color: #333;
  transition: all 0.3s;
}

.action-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.action-icon {
  font-size: 2rem;
}
</style>
