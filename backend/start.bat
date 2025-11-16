@echo off
REM Windows 启动脚本

echo 🚀 启动 SNC Blog FastAPI 服务器...

REM 检查虚拟环境
if not exist "venv" (
    echo 📦 创建虚拟环境...
    python -m venv venv
)

REM 激活虚拟环境
call venv\Scripts\activate.bat

REM 安装依赖
echo 📥 安装依赖...
pip install -r requirements.txt

REM 检查 .env 文件
if not exist ".env" (
    echo ⚠️  未找到 .env 文件，从 .env.example 复制...
    copy .env.example .env
    echo ❗ 请编辑 .env 文件配置必要的环境变量（特别是 JWT_SECRET）
    pause
    exit /b 1
)

REM 启动服务器
echo ✅ 启动服务器...
python run.py
