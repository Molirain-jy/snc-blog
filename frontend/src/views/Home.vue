<script setup lang="ts">
// Hero数据
const heroTitle = '学生网络中心'
const heroSubtitle = '为校园提供优质网络服务 · 推动技术创新与开源文化'

// 服务数据
const services = [
  {
    icon: '🌐',
    title: '网络服务',
    description: '稳定可靠的校园网络，7x24小时运维保障',
    link: '/services'
  },
  {
    icon: '📚',
    title: '技术博客',
    description: '分享技术心得，记录成长历程',
    link: '/blog'
  },
  {
    icon: '🎯',
    title: '活动组织',
    description: '定期举办技术讲座、工作坊和交流活动',
    link: '/events'
  },
  {
    icon: '🔧',
    title: '开源项目',
    description: '维护和贡献开源软件，服务校园师生',
    link: '/services'
  }
]

// 最新活动
const recentEvents = [
  {
    id: 1,
    title: 'Web 开发技术分享会',
    date: '2025-11-15',
    location: '教学楼 A301',
    status: 'upcoming',
    description: '深入探讨现代Web开发技术栈和最佳实践'
  },
  {
    id: 2,
    title: 'Linux 系统运维工作坊',
    date: '2025-11-08',
    location: '实验室 B205',
    status: 'finished',
    description: 'Linux服务器配置、维护与故障排查实战'
  },
  {
    id: 3,
    title: '开源项目贡献指南',
    date: '2025-10-28',
    location: '线上直播',
    status: 'finished',
    description: '如何参与开源项目，从提交第一个PR开始'
  }
]

// 统计数据
const stats = [
  { label: '服务用户', value: '10000+', icon: '👥' },
  { label: '技术文章', value: '200+', icon: '📝' },
  { label: '举办活动', value: '50+', icon: '🎪' },
  { label: '开源项目', value: '30+', icon: '💻' }
]

const scrollToContent = () => {
  window.scrollTo({
    top: window.innerHeight - 70,
    behavior: 'smooth'
  })
}
</script>

<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-background">
        <div class="hero-pattern"></div>
      </div>
      <div class="container">
        <div class="hero-content fade-in">
          <h1 class="hero-title">{{ heroTitle }}</h1>
          <p class="hero-subtitle">{{ heroSubtitle }}</p>
          <div class="hero-actions">
            <router-link to="/about" class="btn btn-primary">
              了解更多
              <span>→</span>
            </router-link>
            <router-link to="/events" class="btn btn-secondary">
              查看活动
            </router-link>
          </div>
          <button @click="scrollToContent" class="scroll-indicator" aria-label="向下滚动">
            <span class="scroll-arrow">↓</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section class="services-section">
      <div class="container">
        <h2 class="section-title">我们的服务</h2>
        <div class="services-grid">
          <router-link
            v-for="service in services"
            :key="service.title"
            :to="service.link"
            class="service-card card"
          >
            <div class="service-icon">{{ service.icon }}</div>
            <h3 class="service-title">{{ service.title }}</h3>
            <p class="service-description">{{ service.description }}</p>
            <span class="service-link">了解更多 →</span>
          </router-link>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="stats-section">
      <div class="container">
        <div class="stats-grid">
          <div v-for="stat in stats" :key="stat.label" class="stat-item">
            <div class="stat-icon">{{ stat.icon }}</div>
            <div class="stat-value">{{ stat.value }}</div>
            <div class="stat-label">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Recent Events Section -->
    <section class="events-section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">最新活动</h2>
          <router-link to="/events" class="view-all">
            查看全部 →
          </router-link>
        </div>
        <div class="events-grid">
          <div
            v-for="event in recentEvents"
            :key="event.id"
            class="event-card card"
          >
            <div class="event-status" :class="event.status">
              {{ event.status === 'upcoming' ? '即将举办' : '已结束' }}
            </div>
            <h3 class="event-title">{{ event.title }}</h3>
            <p class="event-description">{{ event.description }}</p>
            <div class="event-meta">
              <span class="event-date">📅 {{ event.date }}</span>
              <span class="event-location">📍 {{ event.location }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="container">
        <div class="cta-content">
          <h2>加入我们</h2>
          <p>一起探索技术世界，共同成长进步</p>
          <router-link to="/about" class="btn btn-primary">
            立即加入
            <span>→</span>
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Hero Section */
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  /* 背景图片 - 请将图片放在 public/images/hero-bg.jpg */
  background-image: url('/images/hero-bg.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  /* 如果图片未加载，显示渐变色背景 */
  background-color: #99FFFF;
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 0.1;
  z-index: 0;
}

.hero-pattern {
  position: absolute;
  width: 100%;
  height: 100%;
  background-image: 
    repeating-linear-gradient(45deg, transparent, transparent 35px, rgba(255,255,255,.1) 35px, rgba(255,255,255,.1) 70px);
}

.hero-content {
  text-align: center;
  color: white;
  position: relative;
  z-index: 1;
  padding: 40px 0;
}

.hero-title {
  font-size: 4rem;
  font-weight: 700;
  margin-bottom: 24px;
  text-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 48px;
  opacity: 0.95;
  font-weight: 300;
}

.hero-actions {
  display: flex;
  gap: 20px;
  justify-content: center;
  margin-bottom: 80px;
}

.scroll-indicator {
  background: none;
  border: none;
  color: white;
  font-size: 32px;
  cursor: pointer;
  animation: bounce 2s infinite;
  opacity: 0.7;
  transition: opacity 0.3s;
}

.scroll-indicator:hover {
  opacity: 1;
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
}

/* Services Section */
.services-section {
  padding: 80px 0;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 60px;
  color: var(--text-primary);
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 32px;
}

.service-card {
  text-align: center;
  cursor: pointer;
  border: 2px solid transparent;
}

.service-card:hover {
  border-color: var(--primary-color);
}

.service-icon {
  font-size: 3.5rem;
  margin-bottom: 20px;
}

.service-title {
  font-size: 1.5rem;
  margin-bottom: 16px;
  color: var(--text-primary);
}

.service-description {
  color: var(--text-secondary);
  margin-bottom: 20px;
  line-height: 1.8;
}

.service-link {
  color: var(--primary-color);
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

/* Stats Section */
.stats-section {
  padding: 60px 0;
  background: linear-gradient(135deg, #99FFFF 0%, #66CCCC 100%);
  color: #004d4d;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 40px;
}

.stat-item {
  text-align: center;
}

.stat-icon {
  font-size: 3rem;
  margin-bottom: 16px;
}

.stat-value {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 8px;
}

.stat-label {
  font-size: 1.1rem;
  opacity: 0.9;
}

/* Events Section */
.events-section {
  padding: 80px 0;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 48px;
}

.view-all {
  color: var(--primary-color);
  font-weight: 500;
  font-size: 1.1rem;
}

.events-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 32px;
}

.event-card {
  position: relative;
  padding-top: 40px;
}

.event-status {
  position: absolute;
  top: 16px;
  right: 16px;
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
}

.event-status.upcoming {
  background: #e3f2fd;
  color: #1976d2;
}

.event-status.finished {
  background: #f5f5f5;
  color: #757575;
}

.event-title {
  font-size: 1.4rem;
  margin-bottom: 16px;
  color: var(--text-primary);
}

.event-description {
  color: var(--text-secondary);
  margin-bottom: 20px;
  line-height: 1.7;
}

.event-meta {
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 0.95rem;
  color: var(--text-secondary);
}

/* CTA Section */
.cta-section {
  padding: 80px 0;
  background: var(--bg-secondary);
}

.cta-content {
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
}

.cta-content h2 {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.cta-content p {
  font-size: 1.2rem;
  margin-bottom: 40px;
  color: var(--text-secondary);
}

/* 响应式 */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }

  .hero-subtitle {
    font-size: 1.1rem;
  }

  .hero-actions {
    flex-direction: column;
    align-items: center;
  }

  .section-title {
    font-size: 2rem;
  }

  .services-grid,
  .events-grid {
    grid-template-columns: 1fr;
  }

  .section-header {
    flex-direction: column;
    gap: 20px;
    text-align: center;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 32px;
  }
}
</style>
