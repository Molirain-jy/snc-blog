# FastAPI 后端快速参考

## 快速启动

### Windows
```powershell
cd server
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# 编辑 .env 设置 JWT_SECRET
python run.py
```

### Linux/Mac
```bash
cd server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# 编辑 .env 设置 JWT_SECRET
python run.py
```

## 环境变量

```env
MONGODB_URI=mongodb://localhost:27017/snc-blog
JWT_SECRET=your-secret-key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080
CLIENT_URL=http://localhost:3000
PORT=5000
```

## API 端点概览

### 认证
- `GET  /api/auth/check-setup` - 检查初始化状态
- `POST /api/auth/setup` - 创建管理员
- `POST /api/auth/login` - 登录

### 博客
- `GET    /api/blogs` - 获取列表
- `GET    /api/blogs/{id}` - 获取详情
- `POST   /api/blogs` - 创建 🔒
- `PUT    /api/blogs/{id}` - 更新 🔒
- `DELETE /api/blogs/{id}` - 删除 🔒

### 服务
- `GET    /api/services` - 获取列表
- `POST   /api/services` - 创建 🔒
- `PUT    /api/services/{id}` - 更新 🔒
- `DELETE /api/services/{id}` - 删除 🔒

### 活动
- `GET    /api/events` - 获取列表
- `GET    /api/events/{id}` - 获取详情
- `POST   /api/events` - 创建 🔒
- `PUT    /api/events/{id}` - 更新 🔒
- `DELETE /api/events/{id}` - 删除 🔒

### 设置
- `GET    /api/settings` - 获取所有
- `GET    /api/settings/{key}` - 获取单个
- `POST   /api/settings` - 创建/更新 🔒
- `DELETE /api/settings/{key}` - 删除 🔒

🔒 = 需要 Bearer Token

## 常用命令

```bash
# 启动开发服务器（热重载）
uvicorn app.main:app --reload --port 5000

# 生产环境启动
uvicorn app.main:app --host 0.0.0.0 --port 5000 --workers 4

# 运行测试
python test_api.py

# 查看 API 文档
# 浏览器访问 http://localhost:5000/docs
```

## 项目结构

```
server/
├── app/
│   ├── main.py          # 应用入口
│   ├── schemas.py       # 数据模型
│   ├── core/
│   │   ├── config.py    # 配置
│   │   ├── database.py  # 数据库
│   │   └── security.py  # 安全
│   ├── routers/         # API 路由
│   └── middleware/      # 中间件
├── requirements.txt     # 依赖
├── run.py              # 启动脚本
└── .env                # 环境变量
```

## 常见问题

### Q: 如何重置管理员密码？
A: 连接 MongoDB，删除 admins 集合中的文档，重新运行 setup

### Q: 如何添加新的 API 端点？
A: 
1. 在 `schemas.py` 定义数据模型
2. 在 `routers/` 创建路由文件
3. 在 `main.py` 注册路由

### Q: 如何查看日志？
A: FastAPI 使用标准输出，日志会显示在终端

## 性能提示

- 使用异步函数处理所有 I/O 操作
- Motor 驱动自动管理连接池
- Pydantic 自动验证和序列化数据
- FastAPI 自动生成 OpenAPI 文档

## 开发工具

- **API 测试**: http://localhost:5000/docs (Swagger UI)
- **API 文档**: http://localhost:5000/redoc
- **健康检查**: http://localhost:5000/api/health

## 下一步

- 查看 [完整文档](README_FASTAPI.md)
- 阅读 [迁移指南](MIGRATION.md)
- 浏览 [FastAPI 官方文档](https://fastapi.tiangolo.com/)
