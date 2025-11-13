<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

interface Post {
  id: number
  title: string
  excerpt: string
  content: string
  author: string
  date: string
  readTime: string
  category: string
  tags: string[]
  cover?: string
}

const posts = ref<Post[]>([
  {
    id: 1,
    title: 'Vue 3 组合式 API 深度解析',
    excerpt: '探索 Vue 3 Composition API 的设计理念和最佳实践，学习如何使用组合式 API 构建更加灵活和可维护的应用。',
    content: '完整文章内容...',
    author: '张三',
    date: '2025-11-10',
    readTime: '8 分钟',
    category: '前端开发',
    tags: ['Vue', 'JavaScript', '前端']
  },
  {
    id: 2,
    title: 'Linux 服务器性能优化指南',
    excerpt: '从系统配置、网络调优、应用优化等多个维度，全面提升 Linux 服务器性能。包含实战案例和最佳实践。',
    content: '完整文章内容...',
    author: '李四',
    date: '2025-11-08',
    readTime: '12 分钟',
    category: '运维技术',
    tags: ['Linux', '运维', '性能优化']
  },
  {
    id: 3,
    title: 'Docker 容器化部署实践',
    excerpt: '使用 Docker 进行应用容器化的完整指南，包括镜像构建、容器编排、网络配置等核心内容。',
    content: '完整文章内容...',
    author: '王五',
    date: '2025-11-05',
    readTime: '10 分钟',
    category: '运维技术',
    tags: ['Docker', '容器', 'DevOps']
  },
  {
    id: 4,
    title: 'TypeScript 类型体操技巧',
    excerpt: 'TypeScript 高级类型技巧和实用工具类型的深入讲解，帮助你写出更加类型安全的代码。',
    content: '完整文章内容...',
    author: '赵六',
    date: '2025-11-02',
    readTime: '15 分钟',
    category: '前端开发',
    tags: ['TypeScript', 'JavaScript', '类型系统']
  },
  {
    id: 5,
    title: 'Python 异步编程入门',
    excerpt: '深入理解 Python asyncio 库，掌握异步编程的核心概念和应用场景。',
    content: '完整文章内容...',
    author: '孙七',
    date: '2025-10-28',
    readTime: '11 分钟',
    category: '后端开发',
    tags: ['Python', '异步编程', 'asyncio']
  },
  {
    id: 6,
    title: 'Git 工作流最佳实践',
    excerpt: '介绍常见的 Git 工作流模式，包括 Git Flow、GitHub Flow 等，以及团队协作的最佳实践。',
    content: '完整文章内容...',
    author: '周八',
    date: '2025-10-25',
    readTime: '9 分钟',
    category: '开发工具',
    tags: ['Git', '版本控制', '团队协作']
  }
])

const categories = computed(() => {
  const cats = new Set(posts.value.map(p => p.category))
  return ['全部', ...Array.from(cats)]
})

const selectedCategory = ref('全部')
const searchQuery = ref('')

const filteredPosts = computed(() => {
  let result = posts.value

  // 按分类筛选
  if (selectedCategory.value !== '全部') {
    result = result.filter(p => p.category === selectedCategory.value)
  }

  // 按搜索关键词筛选
  if (searchQuery.value.trim()) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(p =>
      p.title.toLowerCase().includes(query) ||
      p.excerpt.toLowerCase().includes(query) ||
      p.tags.some(tag => tag.toLowerCase().includes(query))
    )
  }

  return result
})

const navigateToPost = (id: number) => {
  router.push(`/blog/${id}`)
}
</script>

<template>
  <div class="blog-page">
    <!-- Page Header -->
    <section class="page-header">
      <div class="container">
        <h1 class="page-title fade-in">技术博客</h1>
        <p class="page-subtitle fade-in">分享技术经验，记录成长历程</p>
        
        <!-- Search Box -->
        <div class="search-box">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="搜索文章标题、标签..."
            class="search-input"
          />
          <span class="search-icon">🔍</span>
        </div>
      </div>
    </section>

    <!-- Category Filter -->
    <section class="category-section">
      <div class="container">
        <div class="category-tabs">
          <button
            v-for="category in categories"
            :key="category"
            class="category-tab"
            :class="{ active: selectedCategory === category }"
            @click="selectedCategory = category"
          >
            {{ category }}
          </button>
        </div>
      </div>
    </section>

    <!-- Posts List -->
    <section class="posts-content">
      <div class="container">
        <div v-if="filteredPosts.length > 0" class="posts-grid">
          <article
            v-for="post in filteredPosts"
            :key="post.id"
            class="post-card card"
            @click="navigateToPost(post.id)"
          >
            <div class="post-category">{{ post.category }}</div>
            <h2 class="post-title">{{ post.title }}</h2>
            <p class="post-excerpt">{{ post.excerpt }}</p>
            
            <div class="post-meta">
              <span class="meta-item">
                <span class="icon">👤</span>
                {{ post.author }}
              </span>
              <span class="meta-item">
                <span class="icon">📅</span>
                {{ post.date }}
              </span>
              <span class="meta-item">
                <span class="icon">⏱️</span>
                {{ post.readTime }}
              </span>
            </div>

            <div class="post-tags">
              <span v-for="tag in post.tags" :key="tag" class="tag">
                #{{ tag }}
              </span>
            </div>

            <div class="read-more">
              阅读全文 →
            </div>
          </article>
        </div>

        <div v-else class="empty-state">
          <div class="empty-icon">📝</div>
          <p>没有找到相关文章</p>
          <button @click="searchQuery = ''; selectedCategory = '全部'" class="btn btn-primary">
            查看全部文章
          </button>
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
  margin-bottom: 40px;
}

/* Search Box */
.search-box {
  position: relative;
  max-width: 500px;
  margin: 0 auto;
}

.search-input {
  width: 100%;
  padding: 16px 50px 16px 20px;
  border: none;
  border-radius: 50px;
  font-size: 16px;
  outline: none;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.search-icon {
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 20px;
}

/* Category Section */
.category-section {
  padding: 40px 0;
  background: var(--bg-primary);
  position: sticky;
  top: 70px;
  z-index: 100;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.category-tabs {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
}

.category-tab {
  padding: 10px 20px;
  border: 2px solid var(--primary-color);
  background: white;
  color: var(--primary-color);
  border-radius: var(--radius-lg);
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.category-tab:hover {
  background: var(--primary-light);
  color: white;
  border-color: var(--primary-light);
}

.category-tab.active {
  background: var(--primary-color);
  color: white;
}

/* Posts Content */
.posts-content {
  padding: 60px 0 80px;
}

.posts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 32px;
}

.post-card {
  cursor: pointer;
  position: relative;
  padding: 28px;
  transition: all 0.3s ease;
}

.post-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-lg);
}

.post-category {
  display: inline-block;
  padding: 6px 16px;
  background: var(--primary-color);
  color: white;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
  margin-bottom: 16px;
}

.post-title {
  font-size: 1.5rem;
  margin-bottom: 16px;
  color: var(--text-primary);
  line-height: 1.4;
}

.post-excerpt {
  color: var(--text-secondary);
  line-height: 1.7;
  margin-bottom: 20px;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.post-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--bg-secondary);
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.9rem;
  color: var(--text-secondary);
}

.meta-item .icon {
  font-size: 1rem;
}

.post-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}

.tag {
  padding: 4px 12px;
  background: var(--bg-secondary);
  color: var(--text-secondary);
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 500;
}

.read-more {
  color: var(--primary-color);
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 4px;
  opacity: 0;
  transform: translateX(-10px);
  transition: all 0.3s ease;
}

.post-card:hover .read-more {
  opacity: 1;
  transform: translateX(0);
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
  margin-bottom: 32px;
}

/* 响应式 */
@media (max-width: 768px) {
  .page-title {
    font-size: 2rem;
  }

  .page-subtitle {
    font-size: 1rem;
  }

  .category-section {
    top: 60px;
    padding: 20px 0;
  }

  .posts-grid {
    grid-template-columns: 1fr;
  }

  .post-title {
    font-size: 1.3rem;
  }

  .post-meta {
    flex-direction: column;
    gap: 8px;
  }
}
</style>
