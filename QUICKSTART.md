# 🚀 快速启动指南

## 方式一：Docker 部署（推荐）⭐

### Windows 用户

1. **确保 Docker Desktop 正在运行**

2. **启动项目**
```powershell
.\start.ps1
```

3. **访问应用**
- 前端：http://localhost
- 管理后台：http://localhost/admin

### Linux/Mac 用户

```bash
chmod +x start.sh
./start.sh

# 或直接使用 docker-compose
docker-compose up -d --build
```

## 方式二：本地开发

### 1. 安装依赖

```bash
# 前端依赖
npm install

# 后端依赖
cd server
npm install
cd ..
```

### 2. 配置环境变量

```bash
# 复制环境变量文件
cp server/.env.example server/.env

# 确保 MongoDB 正在运行
# Docker 方式：
docker run -d -p 27017:27017 --name mongodb mongo:7
```

### 3. 启动服务

#### Windows PowerShell
```powershell
.\start-dev.ps1
```

#### 手动启动
```bash
# 终端 1 - 启动后端
cd server
npm run dev

# 终端 2 - 启动前端
npm run dev
```

### 4. 访问应用
- 前端：http://localhost:3000
- 后端 API：http://localhost:5000/api
- 管理后台：http://localhost:3000/admin

## 首次配置管理员

1. 访问 http://localhost/admin （Docker）或 http://localhost:3000/admin （本地）
2. 填写管理员信息：
   - 用户名：admin（或自定义）
   - 邮箱：your@email.com
   - 密码：设置一个强密码
3. 点击"创建账号"
4. 自动登录到管理后台

## 常用命令

### Docker

```bash
# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down

# 重启服务
docker-compose restart

# 完全清理（包括数据）
docker-compose down -v
```

### 开发

```bash
# 前端开发
npm run dev

# 后端开发
cd server
npm run dev

# 构建前端
npm run build

# 预览构建结果
npm run preview
```

## 端口说明

| 服务 | Docker 端口 | 开发端口 |
|------|-------------|----------|
| 前端 | 80 | 3000 |
| 后端 API | 5000 | 5000 |
| MongoDB | 27017 | 27017 |

## 故障排查

### 端口被占用

**Windows:**
```powershell
# 查看端口占用
netstat -ano | findstr :80
netstat -ano | findstr :5000

# 修改 docker-compose.yml 的端口映射
```

### Docker 启动失败

```bash
# 查看错误日志
docker-compose logs

# 强制重新构建
docker-compose up -d --build --force-recreate

# 清理后重启
docker-compose down -v
docker-compose up -d --build
```

### 前端连接不到后端

1. 检查 `.env` 文件中的 `VITE_API_URL`
2. 确认后端服务正在运行
3. 检查浏览器控制台的网络错误

### MongoDB 连接失败

```bash
# Docker 环境
docker-compose restart mongodb
docker-compose logs mongodb

# 本地环境
# 确保 MongoDB 服务正在运行
```

## 下一步

- 📖 阅读 [DEPLOYMENT.md](./DEPLOYMENT.md) 了解详细配置
- 🐳 查看 [DOCKER_README.md](./DOCKER_README.md) 了解 Docker 详情
- 🔧 开始在管理后台创建内容！

## 需要帮助？

- 检查日志文件
- 查看浏览器控制台
- 阅读完整文档
- 提交 Issue

祝你使用愉快！🎉
