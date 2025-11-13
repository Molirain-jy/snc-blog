# SNC Blog - 完整部署指南

## 📋 项目概述

这是一个全栈博客管理系统，包含：
- ✅ Vue 3 + TypeScript 前端
- ✅ Express + MongoDB 后端
- ✅ JWT 认证系统
- ✅ Docker 容器化部署
- ✅ /admin 管理后台
- ✅ 首次登录配置管理员

## 🚀 快速部署（推荐使用 Docker）

### 方式一：使用 PowerShell 脚本（Windows）

```powershell
# 启动所有服务
.\start.ps1

# 或使用 docker-compose
docker-compose up -d --build
```

### 方式二：手动 Docker 命令

```bash
# 1. 构建并启动所有服务
docker-compose up -d --build

# 2. 查看服务状态
docker-compose ps

# 3. 查看日志
docker-compose logs -f

# 4. 停止服务
docker-compose down

# 5. 清理所有数据（包括数据库）
docker-compose down -v
```

## 🔧 本地开发环境

### 前置要求
- Node.js 18+
- MongoDB 5.0+（或使用 Docker）
- npm 或 yarn

### 启动开发环境

#### Windows PowerShell
```powershell
.\start-dev.ps1
```

#### 手动启动

1. **启动 MongoDB**
```bash
# 使用 Docker
docker run -d -p 27017:27017 --name mongodb mongo:7

# 或使用本地 MongoDB
mongod
```

2. **启动后端**
```bash
cd server
npm install
cp .env.example .env
npm run dev
```

3. **启动前端**
```bash
npm install
npm run dev
```

## 📦 服务访问

启动成功后，可访问：

| 服务 | 地址 | 说明 |
|------|------|------|
| 前端网站 | http://localhost | 公开访问的博客网站 |
| 管理后台 | http://localhost/admin | 管理员登录入口 |
| 后端API | http://localhost:5000/api | RESTful API |
| MongoDB | localhost:27017 | 数据库（仅本地访问）|

开发环境：
- 前端：http://localhost:3000
- 后端：http://localhost:5000
- 管理后台：http://localhost:3000/admin

## 🔐 首次使用

1. 访问 `http://localhost/admin`
2. 系统会检测到没有管理员账号，显示配置界面
3. 填写以下信息：
   - 用户名
   - 邮箱
   - 密码
   - 确认密码
4. 点击"创建账号"完成配置
5. 自动登录到管理后台

## 📊 管理功能

登录后可以管理：

### 1. 博客管理 (`/admin/blogs`)
- 创建、编辑、删除文章
- 设置文章分类和标签
- 发布/取消发布文章
- 搜索和筛选文章

### 2. 服务管理 (`/admin/services`)
- 添加服务链接
- 设置服务图标和分类
- 排序服务显示顺序
- 启用/禁用服务

### 3. 活动管理 (`/admin/events`)
- 创建活动信息
- 设置活动时间和地点
- 管理活动状态
- 设置参与人数限制

### 4. 系统设置 (`/admin/settings`)
- 网站基本信息
- 其他系统配置

## 🔌 API 端点

### 认证
```
GET  /api/auth/check-setup  - 检查是否需要初始化
POST /api/auth/setup        - 创建管理员账号
POST /api/auth/login        - 管理员登录
```

### 博客
```
GET    /api/blogs           - 获取所有文章
GET    /api/blogs/:id       - 获取单篇文章
POST   /api/blogs           - 创建文章 [需要认证]
PUT    /api/blogs/:id       - 更新文章 [需要认证]
DELETE /api/blogs/:id       - 删除文章 [需要认证]
```

### 服务
```
GET    /api/services        - 获取所有服务
POST   /api/services        - 创建服务 [需要认证]
PUT    /api/services/:id    - 更新服务 [需要认证]
DELETE /api/services/:id    - 删除服务 [需要认证]
```

### 活动
```
GET    /api/events          - 获取所有活动
GET    /api/events/:id      - 获取单个活动
POST   /api/events          - 创建活动 [需要认证]
PUT    /api/events/:id      - 更新活动 [需要认证]
DELETE /api/events/:id      - 删除活动 [需要认证]
```

## ⚙️ 环境变量配置

### 后端 (server/.env)
```env
PORT=5000
MONGODB_URI=mongodb://mongodb:27017/snc-blog
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
NODE_ENV=production
CLIENT_URL=http://localhost
```

### 前端 (.env)
```env
VITE_API_URL=http://localhost:5000/api
```

### 前端生产环境 (.env.production)
```env
VITE_API_URL=/api
```

## 🐳 Docker 说明

### 服务组成
- **frontend**: Nginx + Vue 应用（端口 80）
- **backend**: Node.js API 服务（端口 5000）
- **mongodb**: MongoDB 数据库（端口 27017）

### 数据持久化
MongoDB 数据存储在 Docker volume `mongodb_data` 中，即使容器删除数据也不会丢失。

要完全清除数据：
```bash
docker-compose down -v
```

### 查看服务
```bash
# 查看运行状态
docker-compose ps

# 查看日志
docker-compose logs frontend
docker-compose logs backend
docker-compose logs mongodb

# 实时日志
docker-compose logs -f
```

## 🔒 安全建议

1. **修改 JWT Secret**
   - 在 `server/.env` 中修改 `JWT_SECRET`
   - 使用强随机字符串（建议 64 字符以上）

2. **使用强密码**
   - 管理员密码建议包含大小写字母、数字和特殊字符
   - 长度至少 12 字符

3. **生产环境**
   - 使用 HTTPS
   - 配置防火墙
   - 限制 MongoDB 端口访问
   - 定期备份数据库
   - 更新依赖包

4. **备份数据**
```bash
# 导出数据库
docker exec snc-blog-mongodb mongodump -d snc-blog -o /backup

# 导入数据库
docker exec snc-blog-mongodb mongorestore -d snc-blog /backup/snc-blog
```

## 📝 开发说明

### 项目结构
```
snc-blog/
├── src/                    # 前端源码
│   ├── views/             # 页面组件
│   │   ├── admin/         # 管理后台
│   │   ├── Blog.vue       # 博客列表
│   │   ├── Services.vue   # 服务页面
│   │   └── Events.vue     # 活动页面
│   ├── components/        # 公共组件
│   ├── utils/            # 工具函数
│   │   └── api.ts        # API 封装
│   └── main.ts           # 入口文件
├── server/                # 后端源码
│   ├── src/
│   │   ├── models/       # Mongoose 模型
│   │   ├── routes/       # Express 路由
│   │   ├── middleware/   # 中间件
│   │   └── index.js      # 服务器入口
│   └── package.json
├── docker-compose.yml     # Docker Compose 配置
├── Dockerfile            # 前端 Dockerfile
└── nginx.conf            # Nginx 配置
```

### 添加新功能

1. **添加新的数据模型**
   - 在 `server/src/models/` 创建模型文件
   - 在 `server/src/routes/` 创建路由文件
   - 在 `server/src/index.js` 中注册路由

2. **添加新的管理页面**
   - 在 `src/views/admin/` 创建组件
   - 在 `src/main.ts` 中添加路由
   - 在 `AdminLayout.vue` 中添加导航项

## 🐛 常见问题

### 1. 端口被占用
```bash
# Windows 查看端口占用
netstat -ano | findstr :80
netstat -ano | findstr :5000

# 修改端口
# 编辑 docker-compose.yml 中的 ports 配置
```

### 2. Docker 容器无法启动
```bash
# 查看详细错误
docker-compose logs

# 重新构建
docker-compose up -d --build --force-recreate
```

### 3. 前端无法连接后端
- 检查 `.env` 中的 `VITE_API_URL` 配置
- 确认后端服务正在运行
- 检查浏览器控制台的 CORS 错误

### 4. MongoDB 连接失败
```bash
# 检查 MongoDB 是否运行
docker-compose ps mongodb

# 重启 MongoDB
docker-compose restart mongodb
```

## 📞 支持

如有问题：
1. 查看 Docker 日志：`docker-compose logs -f`
2. 查看浏览器控制台错误
3. 检查网络连接和端口占用
4. 提交 Issue 到项目仓库

## 📄 许可证

MIT License

---

祝你使用愉快！🎉
