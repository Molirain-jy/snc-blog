from fastapi import APIRouter, HTTPException, status, Depends
from bson import ObjectId
from typing import List
from ..schemas import (
    AdminCreate, AdminLogin, TokenResponse, AdminResponse, MessageResponse
)
from ..core.database import get_database
from ..core.security import get_password_hash, verify_password, create_access_token

router = APIRouter()


@router.get("/check-setup", response_model=dict)
async def check_setup():
    """检查是否已有管理员账号"""
    db = get_database()
    admin_count = await db.admins.count_documents({})
    return {"needsSetup": admin_count == 0}


@router.post("/setup", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def setup_admin(admin: AdminCreate):
    """首次设置管理员账号"""
    db = get_database()
    
    # 检查是否已有管理员
    admin_count = await db.admins.count_documents({})
    if admin_count > 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="管理员账号已存在"
        )
    
    # 创建管理员
    admin_dict = {
        "username": admin.username,
        "email": admin.email,
        "hashed_password": get_password_hash(admin.password),
        "is_first_login": False,
        "created_at": None
    }
    
    result = await db.admins.insert_one(admin_dict)
    
    # 生成令牌
    token = create_access_token({"id": str(result.inserted_id), "username": admin.username})
    
    return TokenResponse(
        message="管理员账号创建成功",
        token=token,
        admin=AdminResponse(id=str(result.inserted_id), username=admin.username, email=admin.email)
    )


@router.post("/login", response_model=TokenResponse)
async def login(credentials: AdminLogin):
    """登录"""
    db = get_database()
    
    # 查找管理员
    admin = await db.admins.find_one({"username": credentials.username})
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误"
        )
    
    # 验证密码
    if not verify_password(credentials.password, admin["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误"
        )
    
    # 生成令牌
    token = create_access_token({"id": str(admin["_id"]), "username": admin["username"]})
    
    return TokenResponse(
        message="登录成功",
        token=token,
        admin=AdminResponse(id=str(admin["_id"]), username=admin["username"], email=admin["email"])
    )
