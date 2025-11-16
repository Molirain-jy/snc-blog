<script setup lang="ts">
const teamMembers = [
  {
    name: '张三',
    role: '技术负责人',
    avatar: '👨‍💻',
    description: '全栈开发工程师，热爱开源',
    skills: ['Vue', 'Node.js', 'Docker']
  },
  {
    name: '李四',
    role: '运维工程师',
    avatar: '👨‍🔧',
    description: 'Linux 系统专家',
    skills: ['Linux', 'Kubernetes', 'CI/CD']
  },
  {
    name: '王五',
    role: '前端开发',
    avatar: '👩‍💻',
    description: '用户界面设计与开发',
    skills: ['React', 'TypeScript', 'UI/UX']
  },
  {
    name: '赵六',
    role: '后端开发',
    avatar: '👨‍💼',
    description: '服务端架构设计',
    skills: ['Python', 'Django', 'PostgreSQL']
  }
]

const timeline = [
  {
    year: '2020',
    title: '社团成立',
    description: '学生网络中心正式成立，开始为校园提供网络服务'
  },
  {
    year: '2021',
    title: '服务扩展',
    description: '推出多项新服务，用户数突破5000+'
  },
  {
    year: '2022',
    title: '技术创新',
    description: '开源多个项目，举办首届技术分享会'
  },
  {
    year: '2023',
    title: '影响力提升',
    description: '与多个高校技术社团建立合作关系'
  },
  {
    year: '2024',
    title: '持续发展',
    description: '服务用户超过10000+，技术团队不断壮大'
  }
]

const values = [
  {
    icon: '🎯',
    title: '追求卓越',
    description: '不断提升技术能力，为用户提供最优质的服务'
  },
  {
    icon: '🤝',
    title: '团队协作',
    description: '相互学习，共同成长，打造高效团队'
  },
  {
    icon: '💡',
    title: '创新精神',
    description: '勇于尝试新技术，推动校园信息化建设'
  },
  {
    icon: '🌍',
    title: '开源分享',
    description: '积极参与开源社区，分享技术经验'
  }
]

const stats = [
  { label: '服务用户', value: '10,000+', icon: '👥' },
  { label: '技术文章', value: '200+', icon: '📝' },
  { label: '举办活动', value: '50+', icon: '🎪' },
  { label: '开源项目', value: '30+', icon: '💻' }
]
</script>

<template>
  <div class="about-page">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="container">
        <div class="hero-content fade-in">
          <h1 class="hero-title">关于我们</h1>
          <p class="hero-subtitle">
            学生网络中心是由技术爱好者组成的团队<br>
            致力于为校园提供优质的网络服务和技术支持
          </p>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="stats-section">
      <div class="container">
        <div class="stats-grid">
          <div v-for="stat in stats" :key="stat.label" class="stat-card">
            <div class="stat-icon">{{ stat.icon }}</div>
            <div class="stat-value">{{ stat.value }}</div>
            <div class="stat-label">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Mission Section -->
    <section class="mission-section">
      <div class="container">
        <h2 class="section-title">我们的使命</h2>
        <div class="mission-content">
          <div class="mission-text">
            <p>
              学生网络中心成立于2020年，是一个由学生自发组织的技术社团。
              我们的目标是为校园师生提供稳定可靠的网络服务，推动校园信息化建设，
              培养学生的技术能力和创新精神。
            </p>
            <p>
              通过定期举办技术讲座、工作坊和交流活动，我们为同学们创造了一个
              学习交流的平台。同时，我们也积极参与开源社区，贡献自己的力量。
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Values Section -->
    <section class="values-section">
      <div class="container">
        <h2 class="section-title">核心价值观</h2>
        <div class="values-grid">
          <div v-for="value in values" :key="value.title" class="value-card card">
            <div class="value-icon">{{ value.icon }}</div>
            <h3 class="value-title">{{ value.title }}</h3>
            <p class="value-description">{{ value.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Team Section -->
    <section class="team-section">
      <div class="container">
        <h2 class="section-title">团队成员</h2>
        <div class="team-grid">
          <div v-for="member in teamMembers" :key="member.name" class="member-card card">
            <div class="member-avatar">{{ member.avatar }}</div>
            <h3 class="member-name">{{ member.name }}</h3>
            <div class="member-role">{{ member.role }}</div>
            <p class="member-description">{{ member.description }}</p>
            <div class="member-skills">
              <span v-for="skill in member.skills" :key="skill" class="skill-tag">
                {{ skill }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Timeline Section -->
    <section class="timeline-section">
      <div class="container">
        <h2 class="section-title">发展历程</h2>
        <div class="timeline">
          <div v-for="(item, _index) in timeline" :key="item.year" class="timeline-item">
            <div class="timeline-marker"></div>
            <div class="timeline-content">
              <div class="timeline-year">{{ item.year }}</div>
              <h3 class="timeline-title">{{ item.title }}</h3>
              <p class="timeline-description">{{ item.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Join Section -->
    <section class="join-section">
      <div class="container">
        <div class="join-content">
          <h2>加入我们</h2>
          <p>如果你热爱技术，愿意分享和学习，欢迎加入我们的团队！</p>
          <div class="join-ways">
            <div class="join-way">
              <div class="join-icon">📧</div>
              <h4>发送邮件</h4>
              <p>contact@snc.edu.cn</p>
            </div>
            <div class="join-way">
              <div class="join-icon">💬</div>
              <h4>加入群组</h4>
              <p>扫码加入我们的交流群</p>
            </div>
            <div class="join-way">
              <div class="join-icon">📝</div>
              <h4>填写表单</h4>
              <p>在线申请加入社团</p>
            </div>
          </div>
          <button class="btn btn-primary">立即申请加入</button>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Hero Section */
.hero-section {
  padding: 100px 0 80px;
  background: linear-gradient(135deg, #99FFFF 0%, #66CCCC 100%);
  color: #004d4d;
  text-align: center;
}

.hero-title {
  font-size: 3.5rem;
  margin-bottom: 24px;
}

.hero-subtitle {
  font-size: 1.3rem;
  line-height: 1.8;
  opacity: 0.95;
}

/* Stats Section */
.stats-section {
  padding: 60px 0;
  background: var(--bg-primary);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 32px;
}

.stat-card {
  text-align: center;
  padding: 32px 20px;
  background: var(--bg-secondary);
  border-radius: var(--radius-lg);
  transition: transform 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-4px);
}

.stat-icon {
  font-size: 3rem;
  margin-bottom: 16px;
}

.stat-value {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--primary-color);
  margin-bottom: 8px;
}

.stat-label {
  font-size: 1.1rem;
  color: var(--text-secondary);
}

/* Mission Section */
.mission-section {
  padding: 80px 0;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 60px;
  color: var(--text-primary);
}

.mission-text {
  max-width: 800px;
  margin: 0 auto;
}

.mission-text p {
  font-size: 1.2rem;
  line-height: 2;
  color: var(--text-secondary);
  margin-bottom: 24px;
}

/* Values Section */
.values-section {
  padding: 80px 0;
  background: var(--bg-secondary);
}

.values-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 32px;
}

.value-card {
  text-align: center;
  padding: 40px 24px;
}

.value-icon {
  font-size: 3.5rem;
  margin-bottom: 24px;
}

.value-title {
  font-size: 1.5rem;
  margin-bottom: 16px;
  color: var(--text-primary);
}

.value-description {
  color: var(--text-secondary);
  line-height: 1.8;
}

/* Team Section */
.team-section {
  padding: 80px 0;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 32px;
}

.member-card {
  text-align: center;
  padding: 32px 24px;
}

.member-avatar {
  font-size: 4rem;
  margin-bottom: 20px;
}

.member-name {
  font-size: 1.5rem;
  margin-bottom: 8px;
  color: var(--text-primary);
}

.member-role {
  display: inline-block;
  padding: 6px 16px;
  background: var(--primary-color);
  color: white;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
  margin-bottom: 16px;
}

.member-description {
  color: var(--text-secondary);
  margin-bottom: 20px;
  line-height: 1.6;
}

.member-skills {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
}

.skill-tag {
  padding: 6px 12px;
  background: var(--bg-secondary);
  color: var(--text-secondary);
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 500;
}

/* Timeline Section */
.timeline-section {
  padding: 80px 0;
  background: var(--bg-secondary);
}

.timeline {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
  padding-left: 40px;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 15px;
  top: 0;
  bottom: 0;
  width: 3px;
  background: var(--primary-color);
}

.timeline-item {
  position: relative;
  margin-bottom: 48px;
}

.timeline-marker {
  position: absolute;
  left: -33px;
  top: 8px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--primary-color);
  border: 3px solid white;
  box-shadow: 0 0 0 3px var(--primary-color);
}

.timeline-content {
  background: white;
  padding: 24px;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
}

.timeline-year {
  display: inline-block;
  padding: 6px 16px;
  background: var(--primary-color);
  color: white;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 12px;
}

.timeline-title {
  font-size: 1.4rem;
  margin-bottom: 12px;
  color: var(--text-primary);
}

.timeline-description {
  color: var(--text-secondary);
  line-height: 1.7;
}

/* Join Section */
.join-section {
  padding: 80px 0;
}

.join-content {
  text-align: center;
  max-width: 900px;
  margin: 0 auto;
}

.join-content h2 {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.join-content > p {
  font-size: 1.2rem;
  color: var(--text-secondary);
  margin-bottom: 48px;
}

.join-ways {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 32px;
  margin-bottom: 48px;
}

.join-way {
  padding: 32px 24px;
  background: var(--bg-secondary);
  border-radius: var(--radius-lg);
  transition: transform 0.3s ease;
}

.join-way:hover {
  transform: translateY(-4px);
}

.join-icon {
  font-size: 3rem;
  margin-bottom: 16px;
}

.join-way h4 {
  font-size: 1.3rem;
  margin-bottom: 12px;
  color: var(--text-primary);
}

.join-way p {
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

  .section-title {
    font-size: 2rem;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .timeline {
    padding-left: 30px;
  }

  .timeline::before {
    left: 10px;
  }

  .timeline-marker {
    left: -28px;
    width: 12px;
    height: 12px;
  }
}
</style>
