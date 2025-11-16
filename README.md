# SNC 学生网络中心 - 全栈博客系统

一个现代化的全栈博客管理系统，采用前后端分离架构。

## ✨ 特性

- 🎨 **现代化设计** - 精美的UI界面，流畅的动画效果
- 📱 **响应式布局** - 完美适配桌面和移动设备
- ⚡ **高性能** - FastAPI 异步后端 + Vite 前端
- 🎯 **TypeScript** - 类型安全，更好的开发体验
- 🔐 **安全认证** - JWT 认证，首次登录配置管理员
- 🐳 **Docker 部署** - 一键部署，前后端分离
- 📝 **内容管理** - 完整的博客、服务、活动管理功能
- 🛡️ **权限控制** - 前台公开访问，后台需要认证
- 📚 **自动文档** - Swagger UI + ReDoc 自动生成 API 文档

## 🏗️ 项目架构

### 前后端分离架构

```
┌─────────────────┐
│   Frontend      │  Vue 3 + TypeScript + Vite
│   (Port 80)     │  用户界面 + 管理后台
└────────┬────────┘
         │ HTTP/REST API
         │
┌────────▼────────┐
│   Backend       │  FastAPI + Python 3.11
│   (Port 5000)   │  RESTful API + JWT 认证
└────────┬────────┘
         │
┌────────▼────────┐
│   MongoDB       │  NoSQL 数据库
│   (Port 27017)  │  数据持久化
└─────────────────┘
```

## 🏗️ 技术栈

### Frontend（前端）
- **Vue 3** - 组合式 API
- **TypeScript** - 类型安全
- **Vite** - 快速构建工具
- **Vue Router** - 路由管理
- **Nginx** - 生产环境 Web 服务器

### Backend（后端）
- **FastAPI** 0.104 - 现代化 Python Web 框架
- **Motor** 3.3 - 异步 MongoDB 驱动
- **Pydantic** 2.5 - 数据验证和序列化
- **Uvicorn** - 高性能 ASGI 服务器
- **Python 3.11+** - 最新 Python 特性

### Database（数据库）
- **MongoDB** 7.0 - NoSQL 文档数据库

### DevOps（部署）
- **Docker** - 容器化
- **Docker Compose** - 多容器编排
- **Nginx** - 反向代理和静态文件服务

## 🚀 快速开始

### 使用 Docker（推荐）

```bash
docker-compose up -d --build
```

访问：
- 前端网站：http://localhost
- 管理后台：http://localhost/admin
- 后端API：http://localhost:5000/api
- API文档：http://localhost:5000/docs

### 本地开发

#### 启动后端
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# 编辑 .env 配置
python run.py
```

#### 启动前端
```bash
cd frontend
npm install
npm run dev
```

#### 启动 MongoDB
```bash
docker run -d -p 27017:27017 --name mongodb mongo:7
```
# 1. 启动 MongoDB
docker run -d -p 27017:27017 --name mongodb mongo:7

# 2. 启动后端（FastAPI）
cd server
pip install -r requirements.txt
cp .env.example .env
# 编辑 .env 文件，设置 JWT_SECRET
python run.py

# 3. 启动前端
cd ..
npm install
npm run dev
```

后端详细文档：[server/README_FASTAPI.md](server/README_FASTAPI.md)

## �️ 自定义图片

### Hero 背景图片

将你的背景图片放在 `public/images/` 文件夹中：

1. 图片命名为 `hero-bg.jpg`（或其他格式如 .png）
2. 推荐分辨率：1920x1080 或更高
3. 建议文件大小：500KB 以内
4. 内容建议：科技感、网络、团队相关的图片

如果使用其他图片名称，请修改 `src/views/Home.vue` 中的路径：
```css
background-image: url('/images/你的图片名.jpg');
```

详细说明请查看 `public/images/README.md`

## 📁 项目结构

```
snc-blog/
├── frontend/                # 前端应用 (Vue 3)
│   ├── src/
│   │   ├── components/     # 公共组件
│   │   ├── views/          # 页面组件
│   │   ├── utils/          # 工具函数
│   │   ├── App.vue         # 根组件
│   │   └── main.ts         # 入口文件
│   ├── public/             # 静态资源
│   ├── index.html          # HTML 模板
│   ├── package.json        # 前端依赖
│   ├── vite.config.ts      # Vite 配置
│   └── Dockerfile          # 前端 Docker 配置
│
├── backend/                # 后端 API (FastAPI)
│   ├── app/
│   │   ├── main.py        # 应用入口
│   │   ├── schemas.py     # 数据模型
│   │   ├── core/          # 核心功能
│   │   ├── routers/       # API 路由
│   │   └── middleware/    # 中间件
│   ├── requirements.txt   # Python 依赖
│   ├── run.py            # 启动脚本
│   └── Dockerfile        # 后端 Docker 配置
│
├── docker-compose.yml     # Docker Compose 配置
└── README.md             # 项目文档
```
│   ├── App.vue              # 根组件
│   ├── main.ts              # 入口文件
│   └── style.css            # 全局样式
├── index.html               # HTML 模板
├── package.json             # 依赖配置
├── tsconfig.json            # TypeScript 配置
└── vite.config.ts           # Vite 配置
```

## 🎯 功能模块

### 首页 (Home)
- Hero 区域，醒目的社团介绍
- 服务展示卡片
- 统计数据展示
- 最新活动预览
- 加入我们的行动号召

### 服务导航 (Services)
- 分类展示各类服务和工具
- 快速访问常用链接
- 卡片式布局，参考 BUCT SNC

### 博客系统 (Blog)
- 文章列表展示
- 分类和搜索功能
- 文章详情页
- 标签系统
- 参考 FSTU 的博客风格

### 活动公告 (Events)
- 活动时间线展示
- 状态筛选（即将举办/已结束）
- 活动详细信息
- 参考 TUNA 的活动展示

### 关于我们 (About)
- 社团介绍
- 团队成员展示
- 发展历程
- 核心价值观
- 加入方式

## 🎨 设计灵感

### TUNA (tuna.moe)
- 清晰的服务展示
- 专业的活动公告样式
- 简洁的配色方案

### FSTU (fstu.cc)
- 优雅的博客文章布局
- 流畅的阅读体验
- 精美的卡片设计

### BUCT SNC (buct.snc.moe)
- 实用的服务导航
- 图标化的链接展示
- 快速访问常用服务

## 🛠️ 技术栈

- **前端框架**: Vue 3 (Composition API)
- **构建工具**: Vite
- **编程语言**: TypeScript
- **路由**: Vue Router
- **样式**: CSS3 (原生 CSS 变量)

## 📝 待办事项

- [ ] 添加后端 API 集成
- [ ] 实现用户评论功能
- [ ] 添加 Markdown 渲染器
- [ ] 实现搜索功能优化
- [ ] 添加深色模式
- [ ] 实现国际化 (i18n)
- [ ] 添加数据统计图表
- [ ] 接入 CMS 内容管理系统

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 👥 联系我们

- Email: contact@snc.edu.cn
- GitHub: https://github.com/snc
- 官网: https://snc.edu.cn

---

**The best team on the campus.** 🌟
