<script setup lang="ts">
import { ref, computed } from 'vue'

interface Event {
  id: number
  title: string
  date: string
  time: string
  location: string
  status: 'upcoming' | 'finished'
  description: string
  speaker?: string
  tags: string[]
  image?: string
}

const events = ref<Event[]>([
  {
    id: 1,
    title: 'Web 开发技术分享会',
    date: '2025-11-15',
    time: '19:00-21:00',
    location: '教学楼 A301',
    status: 'upcoming',
    description: '深入探讨现代Web开发技术栈，包括Vue 3、React、TypeScript等前端技术，以及Node.js后端开发实践。本次分享会将由经验丰富的开发者带来实战经验分享。',
    speaker: '张三 - 前端工程师',
    tags: ['Web开发', '前端', 'JavaScript']
  },
  {
    id: 2,
    title: 'Linux 系统运维工作坊',
    date: '2025-11-08',
    time: '14:00-17:00',
    location: '实验室 B205',
    status: 'finished',
    description: 'Linux服务器配置、维护与故障排查实战。涵盖系统安装、用户管理、权限配置、网络设置、服务管理等核心内容，帮助大家掌握Linux运维的基本技能。',
    speaker: '李四 - 系统运维专家',
    tags: ['Linux', '运维', '服务器']
  },
  {
    id: 3,
    title: '开源项目贡献指南',
    date: '2025-10-28',
    time: '19:30-21:00',
    location: '线上直播',
    status: 'finished',
    description: '如何参与开源项目，从提交第一个PR开始。本次讲座将介绍Git/GitHub的基本使用、如何寻找适合的开源项目、贡献流程和注意事项等。',
    speaker: '王五 - 开源社区贡献者',
    tags: ['开源', 'Git', 'GitHub']
  },
  {
    id: 4,
    title: 'Python 数据分析入门',
    date: '2025-11-22',
    time: '15:00-17:30',
    location: '计算机楼 C102',
    status: 'upcoming',
    description: '使用Python进行数据分析的基础知识，包括NumPy、Pandas、Matplotlib等常用库的使用，以及实际案例分析。',
    speaker: '赵六 - 数据科学家',
    tags: ['Python', '数据分析', 'AI']
  },
  {
    id: 5,
    title: '网络安全与隐私保护',
    date: '2025-10-15',
    time: '18:00-20:00',
    location: '教学楼 A201',
    status: 'finished',
    description: '网络安全基础知识、常见攻击手段及防护措施，个人隐私保护的最佳实践。帮助大家建立安全意识，保护个人信息安全。',
    speaker: '孙七 - 安全工程师',
    tags: ['安全', '隐私', '网络']
  }
])

const selectedFilter = ref<'all' | 'upcoming' | 'finished'>('all')

const filteredEvents = computed(() => {
  if (selectedFilter.value === 'all') {
    return events.value
  }
  return events.value.filter(event => event.status === selectedFilter.value)
})

const upcomingCount = computed(() => 
  events.value.filter(e => e.status === 'upcoming').length
)

const finishedCount = computed(() => 
  events.value.filter(e => e.status === 'finished').length
)
</script>

<template>
  <div class="events-page">
    <!-- Page Header -->
    <section class="page-header">
      <div class="container">
        <h1 class="page-title fade-in">活动公告</h1>
        <p class="page-subtitle fade-in">加入我们的技术活动，一起学习成长</p>
      </div>
    </section>

    <!-- Filter Section -->
    <section class="filter-section">
      <div class="container">
        <div class="filter-tabs">
          <button
            class="filter-tab"
            :class="{ active: selectedFilter === 'all' }"
            @click="selectedFilter = 'all'"
          >
            全部活动 ({{ events.length }})
          </button>
          <button
            class="filter-tab"
            :class="{ active: selectedFilter === 'upcoming' }"
            @click="selectedFilter = 'upcoming'"
          >
            即将举办 ({{ upcomingCount }})
          </button>
          <button
            class="filter-tab"
            :class="{ active: selectedFilter === 'finished' }"
            @click="selectedFilter = 'finished'"
          >
            已结束 ({{ finishedCount }})
          </button>
        </div>
      </div>
    </section>

    <!-- Events List -->
    <section class="events-content">
      <div class="container">
        <div class="events-list">
          <div
            v-for="event in filteredEvents"
            :key="event.id"
            class="event-item card"
          >
            <div class="event-header">
              <div class="event-status-badge" :class="event.status">
                {{ event.status === 'upcoming' ? '即将举办' : '已结束' }}
              </div>
              <div class="event-date-box">
                <div class="month">{{ event.date.split('-')[1] }}月</div>
                <div class="day">{{ event.date.split('-')[2] }}</div>
              </div>
            </div>

            <div class="event-body">
              <h2 class="event-title">{{ event.title }}</h2>
              <p class="event-description">{{ event.description }}</p>

              <div class="event-info">
                <div class="info-item">
                  <span class="icon">🕐</span>
                  <span>{{ event.date }} {{ event.time }}</span>
                </div>
                <div class="info-item">
                  <span class="icon">📍</span>
                  <span>{{ event.location }}</span>
                </div>
                <div v-if="event.speaker" class="info-item">
                  <span class="icon">🎤</span>
                  <span>{{ event.speaker }}</span>
                </div>
              </div>

              <div class="event-tags">
                <span v-for="tag in event.tags" :key="tag" class="tag">
                  {{ tag }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <div v-if="filteredEvents.length === 0" class="empty-state">
          <div class="empty-icon">📅</div>
          <p>暂无相关活动</p>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.page-header {
  padding: 80px 0 60px;
  text-align: center;
  background: linear-gradient(135deg, #99FFFF 0%, #66CCCC 100%);
  color: #004d4d;
}

.page-title {
  font-size: 3rem;
  margin-bottom: 16px;
}

.page-subtitle {
  font-size: 1.2rem;
  opacity: 0.9;
}

/* Filter Section */
.filter-section {
  padding: 40px 0;
  background: var(--bg-primary);
  position: sticky;
  top: 70px;
  z-index: 100;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.filter-tabs {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
}

.filter-tab {
  padding: 12px 24px;
  border: 2px solid var(--primary-color);
  background: white;
  color: var(--primary-color);
  border-radius: var(--radius-lg);
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-tab:hover {
  background: var(--primary-light);
  color: white;
  border-color: var(--primary-light);
}

.filter-tab.active {
  background: var(--primary-color);
  color: white;
}

/* Events Content */
.events-content {
  padding: 60px 0 80px;
}

.events-list {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.event-item {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 32px;
  padding: 32px;
  transition: all 0.3s ease;
}

.event-item:hover {
  transform: translateX(8px);
}

.event-header {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.event-status-badge {
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
  white-space: nowrap;
}

.event-status-badge.upcoming {
  background: #e3f2fd;
  color: #1976d2;
}

.event-status-badge.finished {
  background: #f5f5f5;
  color: #757575;
}

.event-date-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  background: var(--primary-color);
  color: white;
  border-radius: var(--radius-md);
}

.event-date-box .month {
  font-size: 0.9rem;
  opacity: 0.9;
}

.event-date-box .day {
  font-size: 2rem;
  font-weight: 700;
}

.event-body {
  flex: 1;
}

.event-title {
  font-size: 1.75rem;
  margin-bottom: 16px;
  color: var(--text-primary);
}

.event-description {
  color: var(--text-secondary);
  line-height: 1.8;
  margin-bottom: 24px;
}

.event-info {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 20px;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--text-secondary);
  font-size: 0.95rem;
}

.info-item .icon {
  font-size: 1.2rem;
  width: 24px;
}

.event-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  padding: 6px 16px;
  background: var(--bg-secondary);
  color: var(--text-secondary);
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 80px 20px;
}

.empty-icon {
  font-size: 4rem;
  margin-bottom: 20px;
  opacity: 0.5;
}

.empty-state p {
  font-size: 1.2rem;
  color: var(--text-secondary);
}

/* 响应式 */
@media (max-width: 768px) {
  .page-title {
    font-size: 2rem;
  }

  .page-subtitle {
    font-size: 1rem;
  }

  .filter-section {
    top: 60px;
  }

  .event-item {
    grid-template-columns: 1fr;
    gap: 20px;
    padding: 24px;
  }

  .event-header {
    flex-direction: row;
    justify-content: space-between;
  }

  .event-date-box {
    width: 70px;
    height: 70px;
  }

  .event-date-box .day {
    font-size: 1.5rem;
  }

  .event-title {
    font-size: 1.4rem;
  }
}
</style>
