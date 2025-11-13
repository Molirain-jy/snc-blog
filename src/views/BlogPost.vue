<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { marked } from 'marked'

const route = useRoute()
const router = useRouter()

// 配置 marked 选项
marked.setOptions({
  breaks: true,
  gfm: true
})

interface Post {
  id: number
  title: string
  content: string
  author: string
  date: string
  readTime: string
  category: string
  tags: string[]
}

// 模拟文章数据
const posts: Record<number, Post> = {
  1: {
    id: 1,
    title: 'Vue 3 组合式 API 深度解析',
    content: `
# Vue 3 组合式 API 深度解析

## 引言

Vue 3 带来了全新的组合式 API（Composition API），它为我们提供了更灵活的代码组织方式和更好的类型推断。本文将深入探讨组合式 API 的设计理念和最佳实践。

## 为什么需要组合式 API？

在 Vue 2 的选项式 API 中，我们通过不同的选项（data、methods、computed 等）来组织代码。当组件变得复杂时，相关的逻辑会被分散到不同的选项中，导致代码难以维护。

组合式 API 允许我们按照逻辑关注点来组织代码，而不是按照选项类型。

## 核心概念

### 1. setup 函数

\`\`\`javascript
import { ref, computed } from 'vue'

export default {
  setup() {
    const count = ref(0)
    const double = computed(() => count.value * 2)
    
    function increment() {
      count.value++
    }
    
    return {
      count,
      double,
      increment
    }
  }
}
\`\`\`

### 2. 响应式 API

- **ref**: 创建响应式引用
- **reactive**: 创建响应式对象
- **computed**: 计算属性
- **watch**: 侦听器

### 3. 生命周期钩子

\`\`\`javascript
import { onMounted, onUnmounted } from 'vue'

setup() {
  onMounted(() => {
    console.log('组件已挂载')
  })
  
  onUnmounted(() => {
    console.log('组件将卸载')
  })
}
\`\`\`

## 最佳实践

### 1. 组合函数（Composables）

将可复用的逻辑提取到组合函数中：

\`\`\`javascript
// useCounter.js
import { ref } from 'vue'

export function useCounter(initialValue = 0) {
  const count = ref(initialValue)
  
  function increment() {
    count.value++
  }
  
  function decrement() {
    count.value--
  }
  
  return {
    count,
    increment,
    decrement
  }
}
\`\`\`

### 2. TypeScript 支持

组合式 API 提供了更好的 TypeScript 类型推断：

\`\`\`typescript
import { ref, Ref } from 'vue'

interface User {
  name: string
  age: number
}

const user: Ref<User> = ref({
  name: 'John',
  age: 30
})
\`\`\`

## 总结

组合式 API 为 Vue 3 带来了更强大和灵活的开发体验。它不是替代选项式 API，而是提供了一种新的选择。根据项目需求和团队习惯，选择最适合的方式。

## 参考资料

- [Vue 3 官方文档](https://v3.vuejs.org/)
- [Composition API RFC](https://github.com/vuejs/rfcs/blob/master/active-rfcs/0013-composition-api.md)
    `,
    author: '张三',
    date: '2025-11-10',
    readTime: '8 分钟',
    category: '前端开发',
    tags: ['Vue', 'JavaScript', '前端']
  },
  2: {
    id: 2,
    title: 'Linux 服务器性能优化指南',
    content: `
# Linux 服务器性能优化指南

## 简介

服务器性能优化是运维工作中的重要环节。本文将从多个维度介绍 Linux 服务器性能优化的方法和技巧。

## 系统配置优化

### 1. 内核参数调优

编辑 \`/etc/sysctl.conf\`：

\`\`\`bash
# 增加 TCP 连接数
net.ipv4.tcp_max_syn_backlog = 8192
net.core.somaxconn = 8192

# 启用 TCP Fast Open
net.ipv4.tcp_fastopen = 3

# 优化 TCP 缓冲区
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
\`\`\`

应用配置：
\`\`\`bash
sysctl -p
\`\`\`

### 2. 文件描述符限制

编辑 \`/etc/security/limits.conf\`：

\`\`\`
* soft nofile 65535
* hard nofile 65535
\`\`\`

## 性能监控

### 常用监控工具

- **top/htop**: 实时系统监控
- **iostat**: I/O 统计
- **vmstat**: 虚拟内存统计
- **netstat**: 网络连接监控

### 使用示例

\`\`\`bash
# 查看 CPU 使用率
top -bn1 | head -n 5

# 查看磁盘 I/O
iostat -x 1

# 查看网络连接
netstat -tunlp
\`\`\`

## Web 服务器优化

### Nginx 优化

\`\`\`nginx
worker_processes auto;
worker_connections 4096;

keepalive_timeout 65;
keepalive_requests 100;

gzip on;
gzip_comp_level 6;
gzip_types text/plain text/css application/json;
\`\`\`

## 数据库优化

### MySQL 优化建议

1. 合理配置缓冲池大小
2. 使用索引优化查询
3. 定期分析和优化表
4. 启用查询缓存（适用于读多写少的场景）

## 总结

服务器性能优化是一个持续的过程，需要根据实际业务场景进行针对性调整。定期监控和分析是发现性能瓶颈的关键。
    `,
    author: '李四',
    date: '2025-11-08',
    readTime: '12 分钟',
    category: '运维技术',
    tags: ['Linux', '运维', '性能优化']
  }
}

const post = ref<Post | null>(null)
const loading = ref(true)

// 渲染 Markdown 内容
const renderedContent = computed(() => {
  if (!post.value) return ''
  return marked(post.value.content) as string
})

onMounted(() => {
  const postId = Number(route.params.id)
  setTimeout(() => {
    post.value = posts[postId] || null
    loading.value = false
  }, 300)
})

const goBack = () => {
  router.push('/blog')
}

const relatedPosts = [
  { id: 3, title: 'Docker 容器化部署实践', category: '运维技术' },
  { id: 4, title: 'TypeScript 类型体操技巧', category: '前端开发' },
  { id: 5, title: 'Python 异步编程入门', category: '后端开发' }
]
</script>

<template>
  <div class="blog-post-page">
    <div v-if="loading" class="loading-state">
      <div class="loading-spinner"></div>
      <p>加载中...</p>
    </div>

    <div v-else-if="!post" class="error-state">
      <div class="error-icon">😕</div>
      <h2>文章不存在</h2>
      <p>抱歉，您访问的文章不存在或已被删除</p>
      <button @click="goBack" class="btn btn-primary">返回博客列表</button>
    </div>

    <article v-else class="post-content">
      <div class="container">
        <!-- Post Header -->
        <header class="post-header">
          <button @click="goBack" class="back-button">
            ← 返回博客列表
          </button>
          
          <div class="post-category-badge">{{ post.category }}</div>
          <h1 class="post-title">{{ post.title }}</h1>
          
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
        </header>

        <!-- Post Body -->
        <div class="post-body">
          <div class="markdown-content" v-html="renderedContent"></div>
        </div>

        <!-- Post Footer -->
        <footer class="post-footer">
          <div class="share-section">
            <h3>分享文章</h3>
            <div class="share-buttons">
              <button class="share-btn">🔗 复制链接</button>
              <button class="share-btn">📧 邮件分享</button>
              <button class="share-btn">💬 微信分享</button>
            </div>
          </div>

          <div class="related-posts">
            <h3>相关文章</h3>
            <div class="related-list">
              <router-link
                v-for="related in relatedPosts"
                :key="related.id"
                :to="`/blog/${related.id}`"
                class="related-item"
              >
                <span class="related-category">{{ related.category }}</span>
                <span class="related-title">{{ related.title }}</span>
                <span class="related-arrow">→</span>
              </router-link>
            </div>
          </div>
        </footer>
      </div>
    </article>
  </div>
</template>

<style scoped>
.loading-state,
.error-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  text-align: center;
  padding: 40px 20px;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 4px solid var(--bg-secondary);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

.error-icon {
  font-size: 4rem;
  margin-bottom: 20px;
}

.error-state h2 {
  font-size: 2rem;
  margin-bottom: 16px;
}

.error-state p {
  font-size: 1.1rem;
  color: var(--text-secondary);
  margin-bottom: 32px;
}

/* Post Content */
.post-content {
  padding: 40px 0 80px;
}

.post-header {
  max-width: 800px;
  margin: 0 auto 60px;
}

.back-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background: var(--bg-secondary);
  border: none;
  border-radius: var(--radius-md);
  color: var(--text-primary);
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-bottom: 32px;
}

.back-button:hover {
  background: var(--text-secondary);
  color: white;
}

.post-category-badge {
  display: inline-block;
  padding: 8px 20px;
  background: var(--primary-color);
  color: white;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
  margin-bottom: 24px;
}

.post-title {
  font-size: 2.5rem;
  line-height: 1.3;
  margin-bottom: 24px;
  color: var(--text-primary);
}

.post-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  margin-bottom: 24px;
  padding-bottom: 24px;
  border-bottom: 2px solid var(--bg-secondary);
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--text-secondary);
  font-size: 1rem;
}

.meta-item .icon {
  font-size: 1.2rem;
}

.post-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.tag {
  padding: 6px 16px;
  background: var(--bg-secondary);
  color: var(--text-secondary);
  border-radius: 16px;
  font-size: 0.9rem;
  font-weight: 500;
}

/* Post Body */
.post-body {
  max-width: 860px;
  margin: 0 auto 60px;
  background: var(--bg-primary);
  padding: 48px;
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-sm);
}

/* Post Footer */
.post-footer {
  max-width: 800px;
  margin: 0 auto;
}

.share-section,
.related-posts {
  margin-bottom: 48px;
}

.share-section h3,
.related-posts h3 {
  font-size: 1.5rem;
  margin-bottom: 24px;
  color: var(--text-primary);
}

.share-buttons {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.share-btn {
  padding: 12px 24px;
  background: var(--bg-secondary);
  border: none;
  border-radius: var(--radius-md);
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.share-btn:hover {
  background: var(--primary-color);
  color: white;
  transform: translateY(-2px);
}

.related-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.related-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px;
  background: var(--bg-primary);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  transition: all 0.3s ease;
  text-decoration: none;
}

.related-item:hover {
  transform: translateX(8px);
  box-shadow: var(--shadow-md);
}

.related-category {
  padding: 6px 16px;
  background: var(--primary-color);
  color: white;
  border-radius: 16px;
  font-size: 0.85rem;
  font-weight: 500;
  white-space: nowrap;
}

.related-title {
  flex: 1;
  color: var(--text-primary);
  font-weight: 500;
}

.related-arrow {
  color: var(--primary-color);
  font-size: 1.5rem;
}

/* 响应式 */
@media (max-width: 768px) {
  .post-title {
    font-size: 1.75rem;
  }

  .post-body {
    padding: 24px;
  }

  .markdown-content {
    font-size: 1rem;
  }

  .share-buttons {
    flex-direction: column;
  }

  .share-btn {
    width: 100%;
  }

  .related-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }

  .related-arrow {
    display: none;
  }
}
</style>

<!-- Markdown 样式不能用 scoped，因为内容是通过 v-html 插入的 -->
<style>
/* GitHub 风格的 Markdown 样式 */
.markdown-content {
  font-family: "Open Sans", "Clear Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: rgb(51, 51, 51);
  -webkit-font-smoothing: antialiased;
}

.markdown-content a {
  color: #4183C4;
  text-decoration: none;
}

.markdown-content a:hover {
  text-decoration: underline;
}

.markdown-content h1,
.markdown-content h2,
.markdown-content h3,
.markdown-content h4,
.markdown-content h5,
.markdown-content h6 {
  position: relative;
  margin-top: 1rem;
  margin-bottom: 1rem;
  font-weight: bold;
  line-height: 1.4;
  color: rgb(51, 51, 51);
}

.markdown-content h1 {
  font-size: 2.25em;
  line-height: 1.2;
  border-bottom: 1px solid #eee;
  padding-bottom: 0.3em;
}

.markdown-content h2 {
  font-size: 1.75em;
  line-height: 1.225;
  border-bottom: 1px solid #eee;
  padding-bottom: 0.3em;
}

.markdown-content h3 {
  font-size: 1.5em;
  line-height: 1.43;
}

.markdown-content h4 {
  font-size: 1.25em;
}

.markdown-content h5 {
  font-size: 1em;
}

.markdown-content h6 {
  font-size: 1em;
  color: #777;
}

.markdown-content p,
.markdown-content blockquote,
.markdown-content ul,
.markdown-content ol,
.markdown-content dl,
.markdown-content table {
  margin: 0.8em 0;
}

.markdown-content ul,
.markdown-content ol {
  padding-left: 30px;
}

.markdown-content ul li {
  list-style-type: disc;
}

.markdown-content ol li {
  list-style-type: decimal;
}

.markdown-content li > ol,
.markdown-content li > ul {
  margin: 0 0;
}

.markdown-content hr {
  height: 2px;
  padding: 0;
  margin: 16px 0;
  background-color: #e7e7e7;
  border: 0 none;
  overflow: hidden;
}

.markdown-content blockquote {
  border-left: 4px solid #dfe2e5;
  padding: 0 15px;
  color: #777777;
  background: transparent;
}

.markdown-content blockquote blockquote {
  padding-right: 0;
}

.markdown-content table {
  padding: 0;
  word-break: initial;
  border-collapse: collapse;
  width: 100%;
}

.markdown-content table tr {
  border: 1px solid #dfe2e5;
  margin: 0;
  padding: 0;
}

.markdown-content table tr:nth-child(2n),
.markdown-content thead {
  background-color: #f8f8f8;
}

.markdown-content table th {
  font-weight: bold;
  border: 1px solid #dfe2e5;
  border-bottom: 0;
  margin: 0;
  padding: 6px 13px;
  background: #f8f8f8;
}

.markdown-content table td {
  border: 1px solid #dfe2e5;
  margin: 0;
  padding: 6px 13px;
}

.markdown-content table th:first-child,
.markdown-content table td:first-child {
  margin-top: 0;
}

.markdown-content table th:last-child,
.markdown-content table td:last-child {
  margin-bottom: 0;
}

.markdown-content code,
.markdown-content tt {
  border: 1px solid #e7eaed;
  background-color: #f8f8f8;
  border-radius: 3px;
  padding: 2px 4px;
  font-size: 0.9em;
  font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
}

.markdown-content pre {
  margin: 15px 0;
  padding: 16px;
  overflow: auto;
  font-size: 85%;
  line-height: 1.45;
  background-color: #f6f8fa;
  border-radius: 6px;
}

.markdown-content pre code {
  display: inline;
  padding: 0;
  margin: 0;
  overflow: visible;
  line-height: inherit;
  word-wrap: normal;
  background-color: transparent;
  border: 0;
  font-size: inherit;
  color: inherit;
}

.markdown-content img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  margin: 1em 0;
}

.markdown-content strong {
  font-weight: bold;
}

.markdown-content em {
  font-style: italic;
}
</style>
