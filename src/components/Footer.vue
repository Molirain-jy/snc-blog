<script setup lang="ts">
const currentYear = new Date().getFullYear()

const socialLinks = [
  { name: 'GitHub', icon: '💻', url: 'https://github.com' },
  { name: 'Email', icon: '📧', url: 'mailto:contact@snc.edu.cn' },
  { name: 'Telegram', icon: '📱', url: 'https://t.me' }
]

const quickLinks = [
  { name: '首页', path: '/' },
  { name: '服务导航', path: '/services' },
  { name: '博客', path: '/blog' },
  { name: '活动', path: '/events' },
  { name: '关于我们', path: '/about' }
]
</script>

<template>
  <footer class="footer">
    <div class="footer-wave">
      <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M0,0V46.29c47.79,22.2,103.59,32.17,158,28,70.36-5.37,136.33-33.31,206.8-37.5C438.64,32.43,512.34,53.67,583,72.05c69.27,18,138.3,24.88,209.4,13.08,36.15-6,69.85-17.84,104.45-29.34C989.49,25,1113-14.29,1200,52.47V0Z" opacity=".25"></path>
        <path d="M0,0V15.81C13,36.92,27.64,56.86,47.69,72.05,99.41,111.27,165,111,224.58,91.58c31.15-10.15,60.09-26.07,89.67-39.8,40.92-19,84.73-46,130.83-49.67,36.26-2.85,70.9,9.42,98.6,31.56,31.77,25.39,62.32,62,103.63,73,40.44,10.79,81.35-6.69,119.13-24.28s75.16-39,116.92-43.05c59.73-5.85,113.28,22.88,168.9,38.84,30.2,8.66,59,6.17,87.09-7.5,22.43-10.89,48-26.93,60.65-49.24V0Z" opacity=".5"></path>
        <path d="M0,0V5.63C149.93,59,314.09,71.32,475.83,42.57c43-7.64,84.23-20.12,127.61-26.46,59-8.63,112.48,12.24,165.56,35.4C827.93,77.22,886,95.24,951.2,90c86.53-7,172.46-45.71,248.8-84.81V0Z"></path>
      </svg>
    </div>
    
    <div class="footer-content">
      <div class="container">
        <div class="footer-grid">
          <!-- 关于我们 -->
          <div class="footer-section">
            <h3>学生网络中心</h3>
            <p class="footer-description">
              致力于为学校师生提供优质的网络服务和技术支持，推动校园信息化建设。
            </p>
            <div class="social-links">
              <a
                v-for="link in socialLinks"
                :key="link.name"
                :href="link.url"
                :title="link.name"
                class="social-link"
                target="_blank"
                rel="noopener noreferrer"
              >
                <span class="social-icon">{{ link.icon }}</span>
              </a>
            </div>
          </div>

          <!-- 快速链接 -->
          <div class="footer-section">
            <h4>快速链接</h4>
            <ul class="footer-links">
              <li v-for="link in quickLinks" :key="link.path">
                <router-link :to="link.path">{{ link.name }}</router-link>
              </li>
            </ul>
          </div>

          <!-- 联系我们 -->
          <div class="footer-section">
            <h4>联系我们</h4>
            <ul class="contact-info">
              <li>
                <span class="icon">📍</span>
                <span>学校地址</span>
              </li>
              <li>
                <span class="icon">📧</span>
                <span>contact@snc.edu.cn</span>
              </li>
              <li>
                <span class="icon">⏰</span>
                <span>周一至周五 9:00-17:00</span>
              </li>
            </ul>
          </div>
        </div>

        <div class="footer-bottom">
          <p>&copy; {{ currentYear }} 学生网络中心 (SNC). All rights reserved.</p>
          <p class="footer-motto">The best team on the campus.</p>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  position: relative;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  margin-top: 80px;
}

.footer-wave {
  position: absolute;
  top: -1px;
  left: 0;
  width: 100%;
  overflow: hidden;
  line-height: 0;
}

.footer-wave svg {
  position: relative;
  display: block;
  width: calc(100% + 1.3px);
  height: 120px;
}

.footer-wave path {
  fill: var(--bg-secondary);
}

.footer-content {
  padding: 80px 0 40px;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 40px;
  margin-bottom: 40px;
}

.footer-section h3,
.footer-section h4 {
  font-size: 20px;
  margin-bottom: 20px;
  color: white;
}

.footer-description {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.8;
  margin-bottom: 24px;
}

.social-links {
  display: flex;
  gap: 12px;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  transition: all 0.3s ease;
}

.social-link:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-4px);
}

.social-icon {
  font-size: 20px;
}

.footer-links {
  list-style: none;
}

.footer-links li {
  margin-bottom: 12px;
}

.footer-links a {
  color: rgba(255, 255, 255, 0.8);
  transition: all 0.3s ease;
  display: inline-block;
}

.footer-links a:hover {
  color: white;
  transform: translateX(4px);
}

.contact-info {
  list-style: none;
}

.contact-info li {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
  color: rgba(255, 255, 255, 0.8);
}

.contact-info .icon {
  font-size: 20px;
  width: 24px;
}

.footer-bottom {
  padding-top: 40px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  text-align: center;
}

.footer-bottom p {
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 8px;
}

.footer-motto {
  font-style: italic;
  font-size: 14px;
}

@media (max-width: 768px) {
  .footer-content {
    padding: 60px 0 30px;
  }

  .footer-grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }

  .footer-wave svg {
    height: 80px;
  }
}
</style>
