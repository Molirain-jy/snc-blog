# Backend README

SNC Blog 后端 API - 基于 FastAPI + MongoDB

## 技术栈

- **FastAPI** 0.104 - 现代化 Python Web 框架
- **Motor** 3.3 - 异步 MongoDB 驱动
- **Pydantic** 2.5 - 数据验证
- **Uvicorn** - ASGI 服务器
- **Python 3.11+**

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 配置环境变量

创建 `.env` 文件：

```env
MONGODB_URI=mongodb://localhost:27017/snc-blog
JWT_SECRET=your-secret-key-change-this
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080
CLIENT_URL=http://localhost:5173
PORT=5000
```

### 启动服务器

```bash
# 开发模式（热重载）
python run.py

# 或使用 uvicorn
uvicorn app.main:app --reload --port 5000
```

访问：
- API 文档: http://localhost:5000/docs
- ReDoc: http://localhost:5000/redoc
- 健康检查: http://localhost:5000/api/health

## 项目结构

```
backend/
├── app/
│   ├── main.py         # 应用入口
│   ├── schemas.py      # 数据模型
│   ├── core/           # 核心功能
│   ├── routers/        # API 路由
│   └── middleware/     # 中间件
├── requirements.txt    # Python 依赖
└── run.py             # 启动脚本
```

## API 端点

### 认证
- `POST /api/auth/login` - 登录
- `POST /api/auth/setup` - 初始化管理员

### 博客
- `GET /api/blogs` - 获取列表
- `POST /api/blogs` - 创建文章 🔒
- `PUT /api/blogs/{id}` - 更新文章 🔒
- `DELETE /api/blogs/{id}` - 删除文章 🔒

🔒 = 需要认证

## Docker 部署

```bash
# 构建镜像
docker build -t snc-blog-backend .

# 运行容器
docker run -d -p 5000:5000 \
  -e MONGODB_URI=mongodb://host.docker.internal:27017/snc-blog \
  -e JWT_SECRET=your-secret \
  snc-blog-backend
```

## 测试

```bash
python test_api.py
```

## 详细文档

查看以下文档了解更多：
- `README_FASTAPI.md` - 完整文档
- `QUICKSTART.md` - 快速参考
- `ARCHITECTURE.md` - 架构说明

## 许可证

MIT License
