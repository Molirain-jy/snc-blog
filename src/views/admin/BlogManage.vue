<template>
  <div class="blog-manage">
    <div class="header">
      <h1>博客管理</h1>
      <router-link to="/admin/blogs/new" class="btn-primary">
        ➕ 创建新文章
      </router-link>
    </div>

    <div class="filters">
      <input 
        v-model="searchQuery" 
        type="text" 
        placeholder="搜索文章..."
        class="search-input"
      />
      <select v-model="filterCategory" class="filter-select">
        <option value="">全部分类</option>
        <option v-for="cat in categories" :key="cat" :value="cat">{{ cat }}</option>
      </select>
    </div>

    <div class="blog-list">
      <div v-if="loading" class="loading">加载中...</div>
      <div v-else-if="filteredBlogs.length === 0" class="empty">暂无文章</div>
      <div v-else class="blog-items">
        <div v-for="blog in filteredBlogs" :key="blog._id" class="blog-item">
          <div class="blog-info">
            <h3>{{ blog.title }}</h3>
            <p class="excerpt">{{ blog.excerpt }}</p>
            <div class="meta">
              <span class="category">{{ blog.category }}</span>
              <span class="date">{{ formatDate(blog.date) }}</span>
              <span :class="['status', blog.published ? 'published' : 'draft']">
                {{ blog.published ? '已发布' : '草稿' }}
              </span>
            </div>
          </div>
          <div class="blog-actions">
            <router-link :to="`/admin/blogs/edit/${blog._id}`" class="btn-edit">
              编辑
            </router-link>
            <button @click="deleteBlog(blog._id)" class="btn-delete">
              删除
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'

const blogs = ref<any[]>([])
const loading = ref(true)
const searchQuery = ref('')
const filterCategory = ref('')

const categories = computed(() => {
  const cats = new Set(blogs.value.map(b => b.category))
  return Array.from(cats)
})

const filteredBlogs = computed(() => {
  return blogs.value.filter(blog => {
    const matchesSearch = !searchQuery.value || 
      blog.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      blog.excerpt.toLowerCase().includes(searchQuery.value.toLowerCase())
    
    const matchesCategory = !filterCategory.value || blog.category === filterCategory.value
    
    return matchesSearch && matchesCategory
  })
})

onMounted(async () => {
  await loadBlogs()
})

const loadBlogs = async () => {
  try {
    const token = localStorage.getItem('admin_token')
    const res = await fetch(`${API_BASE}/blogs?published=false`, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
    blogs.value = await res.json()
  } catch (error) {
    console.error('加载文章失败:', error)
  } finally {
    loading.value = false
  }
}

const deleteBlog = async (id: string) => {
  if (!confirm('确定要删除这篇文章吗？')) return

  try {
    const token = localStorage.getItem('admin_token')
    const res = await fetch(`${API_BASE}/blogs/${id}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })

    if (res.ok) {
      blogs.value = blogs.value.filter(b => b._id !== id)
    }
  } catch (error) {
    console.error('删除文章失败:', error)
  }
}

const formatDate = (date: string) => {
  return new Date(date).toLocaleDateString('zh-CN')
}
</script>

<style scoped>
.blog-manage {
  max-width: 1200px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.header h1 {
  font-size: 2rem;
  color: #333;
}

.btn-primary {
  background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  transition: transform 0.2s;
}

.btn-primary:hover {
  transform: translateY(-2px);
}

.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.search-input,
.filter-select {
  padding: 0.75rem;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
}

.search-input {
  flex: 1;
}

.filter-select {
  min-width: 150px;
}

.blog-list {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.loading,
.empty {
  text-align: center;
  padding: 2rem;
  color: #666;
}

.blog-items {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.blog-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border: 2px solid #f0f0f0;
  border-radius: 8px;
  transition: border-color 0.3s;
}

.blog-item:hover {
  border-color: #06b6d4;
}

.blog-info {
  flex: 1;
}

.blog-info h3 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  color: #333;
}

.excerpt {
  color: #666;
  margin-bottom: 0.75rem;
  font-size: 0.9rem;
}

.meta {
  display: flex;
  gap: 1rem;
  font-size: 0.85rem;
}

.category {
  background: #06b6d4;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
}

.date {
  color: #999;
}

.status {
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-weight: 600;
}

.status.published {
  background: #e8f5e9;
  color: #2e7d32;
}

.status.draft {
  background: #fff3e0;
  color: #e65100;
}

.blog-actions {
  display: flex;
  gap: 0.5rem;
}

.btn-edit,
.btn-delete {
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-weight: 500;
  cursor: pointer;
  transition: transform 0.2s;
}

.btn-edit {
  background: #06b6d4;
  color: white;
  text-decoration: none;
  border: none;
}

.btn-delete {
  background: #ef5350;
  color: white;
  border: none;
}

.btn-edit:hover,
.btn-delete:hover {
  transform: translateY(-2px);
}
</style>
