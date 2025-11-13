const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'

const getAuthHeaders = () => {
  const token = localStorage.getItem('admin_token')
  return {
    'Content-Type': 'application/json',
    ...(token && { 'Authorization': `Bearer ${token}` })
  }
}

export const api = {
  // 通用请求方法
  async request(endpoint: string, options: RequestInit = {}) {
    const url = `${API_BASE}${endpoint}`
    const config = {
      ...options,
      headers: {
        ...getAuthHeaders(),
        ...options.headers
      }
    }

    try {
      const response = await fetch(url, config)
      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.message || '请求失败')
      }

      return data
    } catch (error) {
      console.error('API Error:', error)
      throw error
    }
  },

  // GET 请求
  get(endpoint: string) {
    return this.request(endpoint, { method: 'GET' })
  },

  // POST 请求
  post(endpoint: string, body: any) {
    return this.request(endpoint, {
      method: 'POST',
      body: JSON.stringify(body)
    })
  },

  // PUT 请求
  put(endpoint: string, body: any) {
    return this.request(endpoint, {
      method: 'PUT',
      body: JSON.stringify(body)
    })
  },

  // DELETE 请求
  delete(endpoint: string) {
    return this.request(endpoint, { method: 'DELETE' })
  },

  // 博客相关
  blogs: {
    getAll: (params?: { category?: string; search?: string; published?: boolean }) => {
      const query = new URLSearchParams()
      if (params?.category) query.append('category', params.category)
      if (params?.search) query.append('search', params.search)
      if (params?.published !== undefined) query.append('published', String(params.published))
      return api.get(`/blogs?${query}`)
    },
    getById: (id: string) => api.get(`/blogs/${id}`),
    create: (data: any) => api.post('/blogs', data),
    update: (id: string, data: any) => api.put(`/blogs/${id}`, data),
    delete: (id: string) => api.delete(`/blogs/${id}`)
  },

  // 服务相关
  services: {
    getAll: (params?: { category?: string; active?: boolean }) => {
      const query = new URLSearchParams()
      if (params?.category) query.append('category', params.category)
      if (params?.active !== undefined) query.append('active', String(params.active))
      return api.get(`/services?${query}`)
    },
    create: (data: any) => api.post('/services', data),
    update: (id: string, data: any) => api.put(`/services/${id}`, data),
    delete: (id: string) => api.delete(`/services/${id}`)
  },

  // 活动相关
  events: {
    getAll: (params?: { category?: string; status?: string; published?: boolean }) => {
      const query = new URLSearchParams()
      if (params?.category) query.append('category', params.category)
      if (params?.status) query.append('status', params.status)
      if (params?.published !== undefined) query.append('published', String(params.published))
      return api.get(`/events?${query}`)
    },
    getById: (id: string) => api.get(`/events/${id}`),
    create: (data: any) => api.post('/events', data),
    update: (id: string, data: any) => api.put(`/events/${id}`, data),
    delete: (id: string) => api.delete(`/events/${id}`)
  },

  // 认证相关
  auth: {
    checkSetup: () => api.get('/auth/check-setup'),
    setup: (data: { username: string; email: string; password: string }) =>
      api.post('/auth/setup', data),
    login: (data: { username: string; password: string }) =>
      api.post('/auth/login', data)
  },

  // 设置相关
  settings: {
    getAll: () => api.get('/settings'),
    get: (key: string) => api.get(`/settings/${key}`),
    set: (data: { key: string; value: any; description?: string }) =>
      api.post('/settings', data),
    delete: (key: string) => api.delete(`/settings/${key}`)
  }
}

export default api
