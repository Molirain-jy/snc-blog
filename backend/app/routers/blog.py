from fastapi import APIRouter, HTTPException, status, Depends, Query
from bson import ObjectId
from typing import List, Optional
from datetime import datetime
from ..schemas import (
    BlogCreate, BlogUpdate, BlogResponse, MessageResponse
)
from ..core.database import get_database
from ..middleware.auth import get_current_user

router = APIRouter()


@router.get("/", response_model=List[BlogResponse])
async def get_blogs(
    category: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    published: Optional[str] = Query("true")
):
    """获取所有文章（公开接口）"""
    db = get_database()
    query = {}
    
    # 只显示已发布的文章
    if published == "true":
        query["published"] = True
    
    if category and category != "全部":
        query["category"] = category
    
    if search:
        query["$or"] = [
            {"title": {"$regex": search, "$options": "i"}},
            {"excerpt": {"$regex": search, "$options": "i"}},
            {"content": {"$regex": search, "$options": "i"}},
            {"tags": {"$regex": search, "$options": "i"}}
        ]
    
    blogs = await db.blogs.find(query).sort("date", -1).to_list(None)
    
    # 转换_id为字符串
    for blog in blogs:
        blog["_id"] = str(blog["_id"])
    
    return blogs


@router.get("/{blog_id}", response_model=BlogResponse)
async def get_blog(blog_id: str):
    """获取单篇文章（公开接口）"""
    db = get_database()
    
    if not ObjectId.is_valid(blog_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的文章ID"
        )
    
    blog = await db.blogs.find_one({"_id": ObjectId(blog_id)})
    
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文章不存在"
        )
    
    blog["_id"] = str(blog["_id"])
    return blog


@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: BlogCreate, current_user: dict = Depends(get_current_user)):
    """创建文章（需要管理员权限）"""
    db = get_database()
    
    blog_dict = blog.model_dump()
    blog_dict["created_at"] = datetime.now()
    blog_dict["updated_at"] = datetime.now()
    
    result = await db.blogs.insert_one(blog_dict)
    
    blog_dict["_id"] = str(result.inserted_id)
    
    return {"message": "文章创建成功", "blog": blog_dict}


@router.put("/{blog_id}", response_model=dict)
async def update_blog(
    blog_id: str,
    blog_update: BlogUpdate,
    current_user: dict = Depends(get_current_user)
):
    """更新文章（需要管理员权限）"""
    db = get_database()
    
    if not ObjectId.is_valid(blog_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的文章ID"
        )
    
    # 只更新提供的字段
    update_data = {k: v for k, v in blog_update.model_dump().items() if v is not None}
    update_data["updated_at"] = datetime.now()
    
    result = await db.blogs.update_one(
        {"_id": ObjectId(blog_id)},
        {"$set": update_data}
    )
    
    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文章不存在"
        )
    
    updated_blog = await db.blogs.find_one({"_id": ObjectId(blog_id)})
    updated_blog["_id"] = str(updated_blog["_id"])
    
    return {"message": "文章更新成功", "blog": updated_blog}


@router.delete("/{blog_id}", response_model=MessageResponse)
async def delete_blog(blog_id: str, current_user: dict = Depends(get_current_user)):
    """删除文章（需要管理员权限）"""
    db = get_database()
    
    if not ObjectId.is_valid(blog_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的文章ID"
        )
    
    result = await db.blogs.delete_one({"_id": ObjectId(blog_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文章不存在"
        )
    
    return MessageResponse(message="文章删除成功")
