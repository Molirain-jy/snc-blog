<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const isScrolled = ref(false)
const isMobileMenuOpen = ref(false)

const navItems = [
  { name: '首页', path: '/' },
  { name: '服务导航', path: '/services' },
  { name: '博客', path: '/blog' },
  { name: '活动', path: '/events' },
  { name: '关于我们', path: '/about' }
]

const handleScroll = () => {
  isScrolled.value = window.scrollY > 20
}

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

const closeMobileMenu = () => {
  isMobileMenuOpen.value = false
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="container">
      <div class="navbar-content">
        <router-link to="/" class="logo" @click="closeMobileMenu">
          <span class="logo-icon">🌐</span>
          <span class="logo-text">SNC</span>
        </router-link>

        <!-- 桌面导航 -->
        <div class="nav-links desktop">
          <router-link
            v-for="item in navItems"
            :key="item.path"
            :to="item.path"
            class="nav-link"
            active-class="active"
          >
            {{ item.name }}
          </router-link>
        </div>

        <!-- 移动端菜单按钮 -->
        <button class="mobile-menu-btn" @click="toggleMobileMenu" aria-label="菜单">
          <span class="hamburger" :class="{ open: isMobileMenuOpen }"></span>
        </button>
      </div>
    </div>

    <!-- 移动端导航菜单 -->
    <Transition name="mobile-menu">
      <div v-if="isMobileMenuOpen" class="mobile-menu">
        <div class="mobile-menu-content">
          <router-link
            v-for="item in navItems"
            :key="item.path"
            :to="item.path"
            class="mobile-nav-link"
            @click="closeMobileMenu"
          >
            {{ item.name }}
          </router-link>
        </div>
      </div>
    </Transition>
  </nav>
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.navbar.scrolled {
  background: rgba(255, 255, 255, 0.98);
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.navbar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 24px;
  font-weight: 700;
  color: var(--primary-color);
  text-decoration: none;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.05);
}

.logo-icon {
  font-size: 28px;
}

.logo-text {
  font-family: 'Courier New', monospace;
}

.nav-links {
  display: flex;
  gap: 32px;
  align-items: center;
}

.nav-links.desktop {
  display: none;
}

.nav-link {
  position: relative;
  color: var(--text-primary);
  font-weight: 500;
  font-size: 15px;
  transition: color 0.3s ease;
  padding: 8px 0;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--primary-color);
  transition: width 0.3s ease;
}

.nav-link:hover,
.nav-link.active {
  color: var(--primary-color);
}

.nav-link:hover::after,
.nav-link.active::after {
  width: 100%;
}

/* 移动端菜单按钮 */
.mobile-menu-btn {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 40px;
  height: 40px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}

.hamburger {
  position: relative;
  width: 24px;
  height: 2px;
  background: var(--text-primary);
  transition: all 0.3s ease;
}

.hamburger::before,
.hamburger::after {
  content: '';
  position: absolute;
  width: 24px;
  height: 2px;
  background: var(--text-primary);
  transition: all 0.3s ease;
}

.hamburger::before {
  top: -8px;
}

.hamburger::after {
  bottom: -8px;
}

.hamburger.open {
  background: transparent;
}

.hamburger.open::before {
  top: 0;
  transform: rotate(45deg);
}

.hamburger.open::after {
  bottom: 0;
  transform: rotate(-45deg);
}

/* 移动端菜单 */
.mobile-menu {
  position: fixed;
  top: 70px;
  left: 0;
  right: 0;
  background: white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  max-height: calc(100vh - 70px);
  overflow-y: auto;
}

.mobile-menu-content {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.mobile-nav-link {
  padding: 16px 20px;
  color: var(--text-primary);
  font-weight: 500;
  font-size: 16px;
  border-radius: var(--radius-md);
  transition: all 0.3s ease;
}

.mobile-nav-link:hover {
  background: var(--bg-secondary);
  color: var(--primary-color);
}

/* 移动端菜单动画 */
.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: all 0.3s ease;
}

.mobile-menu-enter-from,
.mobile-menu-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* 响应式 */
@media (min-width: 769px) {
  .nav-links.desktop {
    display: flex;
  }

  .mobile-menu-btn {
    display: none;
  }
}

@media (max-width: 768px) {
  .navbar-content {
    height: 60px;
  }

  .logo {
    font-size: 20px;
  }

  .logo-icon {
    font-size: 24px;
  }

  .mobile-menu {
    top: 60px;
  }
}
</style>
