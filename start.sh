#!/bin/bash

# 启动 Docker 服务
echo -e "\033[32m正在启动 SNC Blog 服务...\033[0m"
echo ""

# 检查 Docker 是否运行
if ! docker info > /dev/null 2>&1; then
    echo -e "\033[31m错误: Docker 未运行，请先启动 Docker\033[0m"
    exit 1
fi

# 构建并启动服务
echo -e "\033[36m构建并启动所有服务...\033[0m"
docker-compose up -d --build

if [ $? -eq 0 ]; then
    echo ""
    echo -e "\033[32m✅ 服务启动成功!\033[0m"
    echo ""
    echo -e "\033[33m访问地址:\033[0m"
    echo -e "\033[37m  前端网站: http://localhost\033[0m"
    echo -e "\033[37m  管理后台: http://localhost/admin\033[0m"
    echo -e "\033[37m  后端 API: http://localhost:5000/api\033[0m"
    echo ""
    echo -e "\033[36m查看日志: docker-compose logs -f\033[0m"
    echo -e "\033[36m停止服务: docker-compose down\033[0m"
else
    echo ""
    echo -e "\033[31m❌ 服务启动失败\033[0m"
    echo -e "\033[33m请查看错误信息并重试\033[0m"
fi
