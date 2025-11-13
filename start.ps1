# 启动 Docker 服务
Write-Host "正在启动 SNC Blog 服务..." -ForegroundColor Green
Write-Host ""

# 检查 Docker 是否运行
$dockerRunning = docker info 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "错误: Docker 未运行，请先启动 Docker Desktop" -ForegroundColor Red
    exit 1
}

# 构建并启动服务
Write-Host "构建并启动所有服务..." -ForegroundColor Cyan
docker-compose up -d --build

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ 服务启动成功!" -ForegroundColor Green
    Write-Host ""
    Write-Host "访问地址:" -ForegroundColor Yellow
    Write-Host "  前端网站: http://localhost" -ForegroundColor White
    Write-Host "  管理后台: http://localhost/admin" -ForegroundColor White
    Write-Host "  后端 API: http://localhost:5000/api" -ForegroundColor White
    Write-Host ""
    Write-Host "查看日志: docker-compose logs -f" -ForegroundColor Cyan
    Write-Host "停止服务: docker-compose down" -ForegroundColor Cyan
} else {
    Write-Host ""
    Write-Host "❌ 服务启动失败" -ForegroundColor Red
    Write-Host "请查看错误信息并重试" -ForegroundColor Yellow
}
