#!/bin/bash

# 启动脚本
echo "🚀 启动 SNC Blog FastAPI 服务器..."

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
echo "📥 安装依赖..."
pip install -r requirements.txt

# 检查 .env 文件
if [ ! -f ".env" ]; then
    echo "⚠️  未找到 .env 文件，从 .env.example 复制..."
    cp .env.example .env
    echo "❗ 请编辑 .env 文件配置必要的环境变量（特别是 JWT_SECRET）"
    exit 1
fi

# 启动服务器
echo "✅ 启动服务器..."
python run.py
