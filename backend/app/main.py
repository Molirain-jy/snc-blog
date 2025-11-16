from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import os

from .core.config import settings
from .core.database import connect_to_mongo, close_mongo_connection
from .routers import auth, blog, service, event, settings as settings_router

# 创建 FastAPI 应用
app = FastAPI(
    title="SNC Blog API",
    description="Backend API for SNC Blog",
    version="2.0.0"
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.client_url, "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 启动事件
@app.on_event("startup")
async def startup_event():
    """应用启动时执行"""
    await connect_to_mongo()
    
    # 创建uploads目录（如果不存在）
    uploads_dir = "uploads"
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)
    
    print("🚀 FastAPI 服务器启动成功")


# 关闭事件
@app.on_event("shutdown")
async def shutdown_event():
    """应用关闭时执行"""
    await close_mongo_connection()


# 静态文件服务
if os.path.exists("uploads"):
    app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


# 注册路由
app.include_router(auth.router, prefix="/api/auth", tags=["认证"])
app.include_router(blog.router, prefix="/api/blogs", tags=["博客"])
app.include_router(service.router, prefix="/api/services", tags=["服务"])
app.include_router(event.router, prefix="/api/events", tags=["活动"])
app.include_router(settings_router.router, prefix="/api/settings", tags=["设置"])


# 健康检查
@app.get("/api/health", tags=["健康检查"])
async def health_check():
    """健康检查接口"""
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    }


# 根路由
@app.get("/", tags=["根路由"])
async def root():
    """根路由"""
    return {
        "message": "Welcome to SNC Blog API",
        "version": "2.0.0",
        "docs": "/docs"
    }
