# FastAPI 后端快速测试脚本
# 使用方法: .\test-api.ps1

Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 49) -ForegroundColor Cyan
Write-Host "🚀 测试 SNC Blog FastAPI 后端" -ForegroundColor Green
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 49) -ForegroundColor Cyan
Write-Host ""

$baseUrl = "http://localhost:5000"

# 测试健康检查
Write-Host "🔍 测试健康检查..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/api/health" -Method Get
    Write-Host "✅ 健康检查通过" -ForegroundColor Green
    Write-Host "   状态: $($response.status)" -ForegroundColor Gray
    Write-Host "   时间: $($response.timestamp)" -ForegroundColor Gray
    Write-Host ""
} catch {
    Write-Host "❌ 健康检查失败！请确保服务器已启动" -ForegroundColor Red
    Write-Host "   错误: $_" -ForegroundColor Red
    exit 1
}

# 测试初始化状态
Write-Host "🔍 测试检查初始化状态..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/api/auth/check-setup" -Method Get
    Write-Host "✅ 初始化状态检查通过" -ForegroundColor Green
    if ($response.needsSetup) {
        Write-Host "   ⚠️  需要初始化管理员账号" -ForegroundColor Yellow
    } else {
        Write-Host "   ℹ️  管理员账号已存在" -ForegroundColor Cyan
    }
    Write-Host ""
} catch {
    Write-Host "❌ 检查失败: $_" -ForegroundColor Red
}

# 测试获取博客列表
Write-Host "🔍 测试获取博客列表..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/api/blogs" -Method Get
    Write-Host "✅ 获取博客列表成功" -ForegroundColor Green
    Write-Host "   博客数量: $($response.Count)" -ForegroundColor Gray
    Write-Host ""
} catch {
    Write-Host "❌ 获取失败: $_" -ForegroundColor Red
}

# 测试获取服务列表
Write-Host "🔍 测试获取服务列表..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/api/services" -Method Get
    Write-Host "✅ 获取服务列表成功" -ForegroundColor Green
    Write-Host "   服务数量: $($response.Count)" -ForegroundColor Gray
    Write-Host ""
} catch {
    Write-Host "❌ 获取失败: $_" -ForegroundColor Red
}

# 测试获取活动列表
Write-Host "🔍 测试获取活动列表..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/api/events" -Method Get
    Write-Host "✅ 获取活动列表成功" -ForegroundColor Green
    Write-Host "   活动数量: $($response.Count)" -ForegroundColor Gray
    Write-Host ""
} catch {
    Write-Host "❌ 获取失败: $_" -ForegroundColor Red
}

# 总结
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 49) -ForegroundColor Cyan
Write-Host "✅ 基础测试完成！" -ForegroundColor Green
Write-Host ""
Write-Host "📖 访问以下链接查看更多：" -ForegroundColor Cyan
Write-Host "   - API 文档: $baseUrl/docs" -ForegroundColor Gray
Write-Host "   - ReDoc: $baseUrl/redoc" -ForegroundColor Gray
Write-Host "   - 健康检查: $baseUrl/api/health" -ForegroundColor Gray
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 49) -ForegroundColor Cyan
