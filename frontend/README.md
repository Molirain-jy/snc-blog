# Frontend README

SNC Blog 前端应用 - 基于 Vue 3 + TypeScript + Vite

## 技术栈

- **Vue 3** - 渐进式 JavaScript 框架
- **TypeScript** - 类型安全
- **Vite** - 快速构建工具
- **Vue Router** - 路由管理

## 快速开始

### 安装依赖

```bash
npm install
```

### 开发模式

```bash
npm run dev
```

访问 http://localhost:5173

### 构建生产版本

```bash
npm run build
```

构建产物在 `dist/` 目录

### 预览生产构建

```bash
npm run preview
```

## 项目结构

```
frontend/
├── src/
│   ├── components/     # 公共组件
│   ├── views/          # 页面组件
│   ├── utils/          # 工具函数
│   ├── App.vue         # 根组件
│   └── main.ts         # 入口文件
├── public/             # 静态资源
├── index.html          # HTML 模板
└── vite.config.ts      # Vite 配置
```

## 环境变量

创建 `.env` 文件：

```env
VITE_API_URL=http://localhost:5000/api
```

## Docker 部署

```bash
# 构建镜像
docker build -t snc-blog-frontend .

# 运行容器
docker run -d -p 80:80 snc-blog-frontend
```

## 许可证

MIT License
