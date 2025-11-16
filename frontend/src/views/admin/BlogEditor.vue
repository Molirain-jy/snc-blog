<template>
  <div class="blog-editor">
    <div class="header">
      <h1>{{ isEdit ? '编辑文章' : '创建新文章' }}</h1>
      <div class="actions">
        <button @click="router.back()" class="btn-secondary">取消</button>
        <button @click="saveBlog" class="btn-primary" :disabled="saving">
          {{ saving ? '保存中...' : '保存' }}
        </button>
      </div>
    </div>

    <div class="editor-form">
      <div class="form-group">
        <label>标题</label>
        <input v-model="form.title" type="text" placeholder="文章标题" required />
      </div>

      <div class="form-row">
        <div class="form-group">
          <label>作者</label>
          <input v-model="form.author" type="text" placeholder="作者" required />
        </div>
        <div class="form-group">
          <label>分类</label>
          <input v-model="form.category" type="text" placeholder="分类" required />
        </div>
        <div class="form-group">
          <label>阅读时间</label>
          <input v-model="form.readTime" type="text" placeholder="5 分钟" />
        </div>
      </div>

      <div class="form-group">
        <label>标签（用逗号分隔）</label>
        <input v-model="tagsInput" type="text" placeholder="Vue, TypeScript, 前端" />
      </div>

      <div class="form-group">
        <label>摘要</label>
        <textarea v-model="form.excerpt" rows="3" placeholder="文章摘要..." required></textarea>
      </div>

      <div class="form-group">
        <div class="label-with-toggle">
          <label>正文</label>
          <button 
            type="button" 
            @click="showPreview = !showPreview" 
            class="btn-preview"
          >
            {{ showPreview ? '📝 编辑' : '👁️ 预览' }}
          </button>
        </div>
        <textarea 
          v-if="!showPreview"
          v-model="form.content" 
          rows="15" 
          placeholder="支持 Markdown 格式..." 
          required
        ></textarea>
        <div v-else class="markdown-preview" v-html="previewContent"></div>
      </div>

      <div class="form-group">
        <label>
          <input v-model="form.published" type="checkbox" />
          发布文章
        </label>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { marked } from 'marked'

const router = useRouter()
const route = useRoute()
const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'

// 配置 marked
marked.setOptions({
  breaks: true,
  gfm: true
})

const isEdit = computed(() => !!route.params.id)
const saving = ref(false)
const showPreview = ref(false)

const form = ref({
  title: '',
  author: '',
  category: '',
  readTime: '5 分钟',
  excerpt: '',
  content: '',
  published: true,
  tags: [] as string[]
})

const tagsInput = computed({
  get: () => form.value.tags.join(', '),
  set: (val: string) => {
    form.value.tags = val.split(',').map(t => t.trim()).filter(Boolean)
  }
})

// Markdown 预览
const previewContent = computed(() => {
  return marked(form.value.content || '') as string
})

onMounted(async () => {
  if (isEdit.value) {
    await loadBlog()
  }
})

const loadBlog = async () => {
  try {
    const res = await fetch(`${API_BASE}/blogs/${route.params.id}`)
    const blog = await res.json()
    form.value = { ...blog, tags: blog.tags || [] }
  } catch (error) {
    console.error('加载文章失败:', error)
  }
}

const saveBlog = async () => {
  saving.value = true

  try {
    const token = localStorage.getItem('admin_token')
    const method = isEdit.value ? 'PUT' : 'POST'
    const url = isEdit.value 
      ? `${API_BASE}/blogs/${route.params.id}`
      : `${API_BASE}/blogs`

    const res = await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(form.value)
    })

    if (res.ok) {
      router.push('/admin/blogs')
    } else {
      alert('保存失败')
    }
  } catch (error) {
    console.error('保存文章失败:', error)
    alert('保存失败')
  } finally {
    saving.value = false
  }
}
</script>

<style scoped>
.blog-editor {
  max-width: 900px;
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

.actions {
  display: flex;
  gap: 1rem;
}

.btn-primary,
.btn-secondary {
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s;
  border: none;
}

.btn-primary {
  background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
  color: white;
}

.btn-secondary {
  background: #e0e0e0;
  color: #333;
}

.btn-primary:hover:not(:disabled),
.btn-secondary:hover {
  transform: translateY(-2px);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.editor-form {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.form-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #333;
  font-weight: 500;
}

.form-group input[type="text"],
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
  font-family: inherit;
}

.form-group input[type="checkbox"] {
  margin-right: 0.5rem;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #06b6d4;
}

.label-with-toggle {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.btn-preview {
  padding: 0.5rem 1rem;
  background: #06b6d4;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-preview:hover {
  background: #0891b2;
  transform: translateY(-2px);
}
</style>

<!-- Markdown 预览样式不能用 scoped，因为内容是通过 v-html 插入的 -->
<style>
.markdown-preview {
  min-height: 400px;
  padding: 2rem;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  background: white;
  overflow-y: auto;
  font-family: "Open Sans", "Clear Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: rgb(51, 51, 51);
}

/* GitHub 风格的 Markdown 预览样式 */
.markdown-preview h1,
.markdown-preview h2,
.markdown-preview h3,
.markdown-preview h4,
.markdown-preview h5,
.markdown-preview h6 {
  position: relative;
  margin-top: 1rem;
  margin-bottom: 1rem;
  font-weight: bold;
  line-height: 1.4;
}

.markdown-preview h1 {
  font-size: 2.25em;
  line-height: 1.2;
  border-bottom: 1px solid #eee;
  padding-bottom: 0.3em;
}

.markdown-preview h2 {
  font-size: 1.75em;
  line-height: 1.225;
  border-bottom: 1px solid #eee;
  padding-bottom: 0.3em;
}

.markdown-preview h3 {
  font-size: 1.5em;
  line-height: 1.43;
}

.markdown-preview h4 {
  font-size: 1.25em;
}

.markdown-preview h5 {
  font-size: 1em;
}

.markdown-preview h6 {
  font-size: 1em;
  color: #777;
}

.markdown-preview p,
.markdown-preview blockquote,
.markdown-preview ul,
.markdown-preview ol,
.markdown-preview dl,
.markdown-preview table {
  margin: 0.8em 0;
}

.markdown-preview a {
  color: #4183C4;
  text-decoration: none;
}

.markdown-preview a:hover {
  text-decoration: underline;
}

.markdown-preview ul,
.markdown-preview ol {
  padding-left: 30px;
}

.markdown-preview ul li {
  list-style-type: disc;
}

.markdown-preview ol li {
  list-style-type: decimal;
}

.markdown-preview li > ol,
.markdown-preview li > ul {
  margin: 0 0;
}

.markdown-preview hr {
  height: 2px;
  padding: 0;
  margin: 16px 0;
  background-color: #e7e7e7;
  border: 0 none;
}

.markdown-preview blockquote {
  border-left: 4px solid #dfe2e5;
  padding: 0 15px;
  color: #777777;
  background: transparent;
}

.markdown-preview table {
  padding: 0;
  word-break: initial;
  border-collapse: collapse;
  width: 100%;
}

.markdown-preview table tr {
  border: 1px solid #dfe2e5;
  margin: 0;
  padding: 0;
}

.markdown-preview table tr:nth-child(2n),
.markdown-preview thead {
  background-color: #f8f8f8;
}

.markdown-preview table th {
  font-weight: bold;
  border: 1px solid #dfe2e5;
  border-bottom: 0;
  margin: 0;
  padding: 6px 13px;
}

.markdown-preview table td {
  border: 1px solid #dfe2e5;
  margin: 0;
  padding: 6px 13px;
}

.markdown-preview code,
.markdown-preview tt {
  border: 1px solid #e7eaed;
  background-color: #f8f8f8;
  border-radius: 3px;
  padding: 2px 4px;
  font-size: 0.9em;
  font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
}

.markdown-preview pre {
  margin: 15px 0;
  padding: 16px;
  overflow: auto;
  font-size: 85%;
  line-height: 1.45;
  background-color: #f6f8fa;
  border-radius: 6px;
}

.markdown-preview pre code {
  display: inline;
  padding: 0;
  margin: 0;
  overflow: visible;
  line-height: inherit;
  word-wrap: normal;
  background-color: transparent;
  border: 0;
}

.markdown-preview img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  margin: 1em 0;
}

.markdown-preview strong {
  font-weight: bold;
}

.markdown-preview em {
  font-style: italic;
}
</style>

