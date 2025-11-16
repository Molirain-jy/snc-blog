"""
简单的 API 测试脚本
运行前请确保服务器已启动
"""
import requests
import json

BASE_URL = "http://localhost:5000"


def test_health():
    """测试健康检查"""
    print("🔍 测试健康检查...")
    response = requests.get(f"{BASE_URL}/api/health")
    print(f"状态码: {response.status_code}")
    print(f"响应: {response.json()}")
    assert response.status_code == 200
    print("✅ 健康检查通过\n")


def test_check_setup():
    """测试是否需要初始化"""
    print("🔍 测试检查初始化状态...")
    response = requests.get(f"{BASE_URL}/api/auth/check-setup")
    print(f"状态码: {response.status_code}")
    print(f"响应: {response.json()}")
    assert response.status_code == 200
    print("✅ 初始化检查通过\n")
    return response.json()


def test_create_admin():
    """测试创建管理员（仅在需要时）"""
    setup_status = test_check_setup()
    
    if not setup_status.get("needsSetup"):
        print("⚠️ 管理员已存在，跳过创建\n")
        return None
    
    print("🔍 测试创建管理员...")
    admin_data = {
        "username": "admin",
        "password": "admin123",
        "email": "admin@example.com"
    }
    
    response = requests.post(f"{BASE_URL}/api/auth/setup", json=admin_data)
    print(f"状态码: {response.status_code}")
    print(f"响应: {response.json()}")
    assert response.status_code == 201
    print("✅ 管理员创建成功\n")
    return response.json()


def test_login():
    """测试登录"""
    print("🔍 测试登录...")
    login_data = {
        "username": "admin",
        "password": "admin123"
    }
    
    response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
    print(f"状态码: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Token: {data['token'][:50]}...")
        print("✅ 登录成功\n")
        return data["token"]
    else:
        print(f"❌ 登录失败: {response.json()}")
        return None


def test_get_blogs():
    """测试获取博客列表"""
    print("🔍 测试获取博客列表...")
    response = requests.get(f"{BASE_URL}/api/blogs")
    print(f"状态码: {response.status_code}")
    print(f"博客数量: {len(response.json())}")
    assert response.status_code == 200
    print("✅ 获取博客列表成功\n")


def test_create_blog(token):
    """测试创建博客"""
    print("🔍 测试创建博客...")
    headers = {"Authorization": f"Bearer {token}"}
    blog_data = {
        "title": "测试文章",
        "excerpt": "这是一篇测试文章的摘要",
        "content": "这是测试文章的完整内容...",
        "author": "测试作者",
        "category": "技术",
        "tags": ["测试", "FastAPI"],
        "published": True
    }
    
    response = requests.post(f"{BASE_URL}/api/blogs", json=blog_data, headers=headers)
    print(f"状态码: {response.status_code}")
    
    if response.status_code == 201:
        data = response.json()
        print(f"博客ID: {data['blog']['_id']}")
        print("✅ 创建博客成功\n")
        return data["blog"]["_id"]
    else:
        print(f"❌ 创建失败: {response.json()}")
        return None


def test_get_services():
    """测试获取服务列表"""
    print("🔍 测试获取服务列表...")
    response = requests.get(f"{BASE_URL}/api/services")
    print(f"状态码: {response.status_code}")
    print(f"服务数量: {len(response.json())}")
    assert response.status_code == 200
    print("✅ 获取服务列表成功\n")


def test_get_events():
    """测试获取活动列表"""
    print("🔍 测试获取活动列表...")
    response = requests.get(f"{BASE_URL}/api/events")
    print(f"状态码: {response.status_code}")
    print(f"活动数量: {len(response.json())}")
    assert response.status_code == 200
    print("✅ 获取活动列表成功\n")


def run_all_tests():
    """运行所有测试"""
    print("=" * 50)
    print("🚀 开始测试 FastAPI 后端")
    print("=" * 50 + "\n")
    
    try:
        # 基础测试
        test_health()
        
        # 认证测试
        test_check_setup()
        test_create_admin()
        token = test_login()
        
        # API 测试
        test_get_blogs()
        test_get_services()
        test_get_events()
        
        # 需要认证的测试
        if token:
            test_create_blog(token)
        
        print("=" * 50)
        print("✅ 所有测试通过！")
        print("=" * 50)
        
    except requests.exceptions.ConnectionError:
        print("❌ 连接失败！请确保服务器已启动在 http://localhost:5000")
    except AssertionError as e:
        print(f"❌ 测试失败: {e}")
    except Exception as e:
        print(f"❌ 发生错误: {e}")


if __name__ == "__main__":
    run_all_tests()
