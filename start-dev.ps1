# 开发环境启动脚本

Write-Host "启动开发环境..." -ForegroundColor Green
Write-Host ""

# 检查是否安装了依赖
if (-not (Test-Path "node_modules")) {
    Write-Host "正在安装前端依赖..." -ForegroundColor Cyan
    npm install
}

if (-not (Test-Path "server/node_modules")) {
    Write-Host "正在安装后端依赖..." -ForegroundColor Cyan
    cd server
    npm install
    cd ..
}

# 启动 MongoDB (需要本地安装)
Write-Host ""
Write-Host "请确保 MongoDB 正在运行 (mongodb://localhost:27017)" -ForegroundColor Yellow
Write-Host ""

# 启动后端
Write-Host "启动后端服务..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\server'; npm run dev"

# 等待后端启动
Start-Sleep -Seconds 3

# 启动前端
Write-Host "启动前端服务..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD'; npm run dev"

Write-Host ""
Write-Host "✅ 开发环境启动完成!" -ForegroundColor Green
Write-Host ""
Write-Host "前端将在 http://localhost:3000 运行" -ForegroundColor White
Write-Host "后端将在 http://localhost:5000 运行" -ForegroundColor White
Write-Host "管理后台: http://localhost:3000/admin" -ForegroundColor White
