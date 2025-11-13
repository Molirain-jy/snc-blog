# SNC Blog - 全栈博客系统

一个基于 Vue 3 + Express + MongoDB 的全栈博客系统，支持文章、服务、活动管理。

## 功能特性

- 📝 **博客管理** - 完整的文章创建、编辑、删除功能
- 🔗 **服务管理** - 管理各类服务链接
- 📅 **活动管理** - 发布和管理活动信息
- 🔐 **安全认证** - JWT 认证，首次登录配置管理员账号
- 🐳 **Docker 部署** - 一键部署，包含前端、后端、数据库
- 📱 **响应式设计** - 适配各种设备

## 技术栈

### 前端
- Vue 3 + TypeScript
- Vue Router
- Vite

### 后端
- Node.js + Express
- MongoDB + Mongoose
- JWT 认证
- bcryptjs 密码加密

### 部署
- Docker + Docker Compose
- Nginx

## 快速开始

### 使用 Docker（推荐）

1. 克隆项目
```bash
git clone <repository-url>
cd snc-blog
```

2. 配置环境变量（可选）
```bash
cp server/.env.example server/.env
# 编辑 server/.env 修改配置
```

3. 启动所有服务
```bash
docker-compose up -d
```

4. 访问应用
- 前端：http://localhost
- 后端 API：http://localhost:5000/api
- 管理后台：http://localhost/admin

### 本地开发

#### 后端开发

```bash
cd server
npm install
cp .env.example .env
npm run dev
```

#### 前端开发

```bash
npm install
npm run dev
```

## 首次使用

1. 启动应用后，访问 `http://localhost/admin`
2. 首次访问会提示配置管理员账号
3. 填写用户名、邮箱、密码完成配置
4. 登录后即可管理所有内容

## 管理功能

访问 `/admin` 进入管理后台：

- **仪表盘** - 查看数据统计
- **博客管理** - 创建、编辑、删除文章
- **服务管理** - 管理服务链接
- **活动管理** - 管理活动信息
- **系统设置** - 配置系统参数

## API 接口

### 认证接口
- `GET /api/auth/check-setup` - 检查是否需要首次设置
- `POST /api/auth/setup` - 首次设置管理员账号
- `POST /api/auth/login` - 管理员登录

### 博客接口
- `GET /api/blogs` - 获取所有文章
- `GET /api/blogs/:id` - 获取单篇文章
- `POST /api/blogs` - 创建文章（需要认证）
- `PUT /api/blogs/:id` - 更新文章（需要认证）
- `DELETE /api/blogs/:id` - 删除文章（需要认证）

### 服务接口
- `GET /api/services` - 获取所有服务
- `POST /api/services` - 创建服务（需要认证）
- `PUT /api/services/:id` - 更新服务（需要认证）
- `DELETE /api/services/:id` - 删除服务（需要认证）

### 活动接口
- `GET /api/events` - 获取所有活动
- `GET /api/events/:id` - 获取单个活动
- `POST /api/events` - 创建活动（需要认证）
- `PUT /api/events/:id` - 更新活动（需要认证）
- `DELETE /api/events/:id` - 删除活动（需要认证）

## 项目结构

```
snc-blog/
├── src/                      # 前端源码
│   ├── views/               # 页面组件
│   │   ├── admin/          # 管理后台页面
│   │   └── ...             # 其他页面
│   ├── components/          # 公共组件
│   ├── App.vue             # 根组件
│   └── main.ts             # 入口文件
├── server/                   # 后端源码
│   ├── src/
│   │   ├── models/         # 数据模型
│   │   ├── routes/         # API 路由
│   │   ├── middleware/     # 中间件
│   │   └── index.js        # 入口文件
│   └── package.json
├── docker-compose.yml        # Docker Compose 配置
├── Dockerfile               # 前端 Dockerfile
└── nginx.conf               # Nginx 配置
```

## 环境变量

### 后端环境变量 (server/.env)

```env
PORT=5000
MONGODB_URI=mongodb://mongodb:27017/snc-blog
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
NODE_ENV=production
CLIENT_URL=http://localhost
```

## Docker 命令

```bash
# 启动所有服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止所有服务
docker-compose down

# 重新构建并启动
docker-compose up -d --build

# 清理数据（包括数据库）
docker-compose down -v
```

## 安全建议

1. **修改 JWT_SECRET** - 在生产环境中务必修改为强密码
2. **HTTPS** - 生产环境使用 HTTPS
3. **定期备份** - 定期备份 MongoDB 数据
4. **强密码** - 使用强密码作为管理员密码
5. **防火墙** - 配置防火墙规则，限制数据库端口访问

## 许可证

MIT License

## 支持

如有问题，请提交 Issue 或 Pull Request。
