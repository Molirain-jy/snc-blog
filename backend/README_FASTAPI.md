# SNC Blog - FastAPI 后端

基于 FastAPI 的博客系统后端 API。

## 技术栈

- **FastAPI**: 现代化、快速的 Web 框架
- **Motor**: MongoDB 异步驱动
- **Pydantic**: 数据验证和设置管理
- **JWT**: JSON Web Token 认证
- **Uvicorn**: ASGI 服务器

## 项目结构

```
server/
├── app/
│   ├── __init__.py
│   ├── main.py              # 应用入口
│   ├── schemas.py           # Pydantic 数据模型
│   ├── core/
│   │   ├── config.py       # 配置管理
│   │   ├── database.py     # 数据库连接
│   │   └── security.py     # 安全相关（JWT、密码加密）
│   ├── routers/
│   │   ├── auth.py         # 认证路由
│   │   ├── blog.py         # 博客路由
│   │   ├── service.py      # 服务路由
│   │   ├── event.py        # 活动路由
│   │   └── settings.py     # 设置路由
│   └── middleware/
│       └── auth.py         # 认证中间件
├── uploads/                 # 上传文件目录
├── requirements.txt        # Python 依赖
├── run.py                  # 开发服务器启动脚本
├── Dockerfile             # Docker 配置
└── .env                   # 环境变量配置
```

## 快速开始

### 环境要求

- Python 3.11+
- MongoDB 4.0+

### 安装依赖

```bash
cd server
pip install -r requirements.txt
```

### 配置环境变量

创建 `.env` 文件：

```env
# MongoDB Configuration
MONGODB_URI=mongodb://localhost:27017/snc-blog

# JWT Configuration
JWT_SECRET=your-secret-key-here-change-in-production
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# CORS Configuration
CLIENT_URL=http://localhost:3000

# Server Configuration
PORT=5000
```

### 运行开发服务器

```bash
# 方式 1：使用 run.py
python run.py

# 方式 2：直接使用 uvicorn
uvicorn app.main:app --reload --port 5000
```

服务器将在 http://localhost:5000 启动

### API 文档

FastAPI 自动生成交互式 API 文档：

- **Swagger UI**: http://localhost:5000/docs
- **ReDoc**: http://localhost:5000/redoc

## API 端点

### 认证 (`/api/auth`)

- `GET /api/auth/check-setup` - 检查是否需要初始化管理员
- `POST /api/auth/setup` - 首次设置管理员账号
- `POST /api/auth/login` - 管理员登录

### 博客 (`/api/blogs`)

- `GET /api/blogs` - 获取所有文章（支持分类、搜索）
- `GET /api/blogs/{id}` - 获取单篇文章
- `POST /api/blogs` - 创建文章 🔒
- `PUT /api/blogs/{id}` - 更新文章 🔒
- `DELETE /api/blogs/{id}` - 删除文章 🔒

### 服务 (`/api/services`)

- `GET /api/services` - 获取所有服务
- `POST /api/services` - 创建服务 🔒
- `PUT /api/services/{id}` - 更新服务 🔒
- `DELETE /api/services/{id}` - 删除服务 🔒

### 活动 (`/api/events`)

- `GET /api/events` - 获取所有活动
- `GET /api/events/{id}` - 获取单个活动
- `POST /api/events` - 创建活动 🔒
- `PUT /api/events/{id}` - 更新活动 🔒
- `DELETE /api/events/{id}` - 删除活动 🔒

### 设置 (`/api/settings`)

- `GET /api/settings` - 获取所有设置
- `GET /api/settings/{key}` - 获取单个设置
- `POST /api/settings` - 创建/更新设置 🔒
- `DELETE /api/settings/{key}` - 删除设置 🔒

🔒 = 需要管理员认证

## Docker 部署

### 构建镜像

```bash
docker build -t snc-blog-server .
```

### 运行容器

```bash
docker run -d \
  -p 5000:5000 \
  -e MONGODB_URI=mongodb://host.docker.internal:27017/snc-blog \
  -e JWT_SECRET=your-secret-key \
  --name snc-blog-server \
  snc-blog-server
```

### 使用 Docker Compose

```bash
docker-compose up -d
```

## 开发指南

### 添加新路由

1. 在 `app/schemas.py` 中定义 Pydantic 模型
2. 在 `app/routers/` 中创建新路由文件
3. 在 `app/main.py` 中注册路由

### 数据库操作

```python
from app.core.database import get_database

# 在路由函数中
db = get_database()
result = await db.collection_name.find_one({"_id": ObjectId(id)})
```

### 认证保护

```python
from app.middleware.auth import get_current_user
from fastapi import Depends

@router.post("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    # 需要认证的路由
    pass
```

## 性能优化

- 使用 Motor 异步驱动实现非阻塞 I/O
- Pydantic 数据验证提高类型安全
- FastAPI 自动生成 OpenAPI 文档
- 支持自动数据序列化和反序列化

## 从 Express 迁移注意事项

### 主要变化

1. **异步处理**: 所有数据库操作使用 `async/await`
2. **类型验证**: 使用 Pydantic 模型进行自动验证
3. **路径参数**: 使用 `{param}` 而不是 `:param`
4. **依赖注入**: 使用 FastAPI 的依赖注入系统
5. **中间件**: 使用装饰器和依赖项进行认证

### 数据库兼容性

MongoDB 数据无需迁移，可以直接使用现有数据库。ObjectId 会自动转换为字符串。

## 测试

```bash
# 安装测试依赖
pip install pytest pytest-asyncio httpx

# 运行测试
pytest
```

## 常见问题

### Q: 如何修改端口？

A: 在 `.env` 文件中修改 `PORT` 变量。

### Q: 如何启用 HTTPS？

A: 在生产环境中，建议使用 Nginx 作为反向代理来处理 SSL/TLS。

### Q: 如何处理文件上传？

A: FastAPI 支持文件上传，使用 `UploadFile` 类型即可。

## 许可证

MIT License
