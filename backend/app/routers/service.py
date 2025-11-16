from fastapi import APIRouter, HTTPException, status, Depends, Query
from bson import ObjectId
from typing import List, Optional
from datetime import datetime
from ..schemas import (
    ServiceCreate, ServiceUpdate, ServiceResponse, MessageResponse
)
from ..core.database import get_database
from ..middleware.auth import get_current_user

router = APIRouter()


@router.get("/", response_model=List[ServiceResponse])
async def get_services(
    category: Optional[str] = Query(None),
    active: Optional[str] = Query("true")
):
    """获取所有服务（公开接口）"""
    db = get_database()
    query = {}
    
    if active == "true":
        query["active"] = True
    
    if category and category != "全部":
        query["category"] = category
    
    services = await db.services.find(query).sort([("order", 1), ("created_at", -1)]).to_list(None)
    
    for service in services:
        service["_id"] = str(service["_id"])
    
    return services


@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_service(service: ServiceCreate, current_user: dict = Depends(get_current_user)):
    """创建服务（需要管理员权限）"""
    db = get_database()
    
    service_dict = service.model_dump()
    service_dict["created_at"] = datetime.now()
    
    result = await db.services.insert_one(service_dict)
    
    service_dict["_id"] = str(result.inserted_id)
    
    return {"message": "服务创建成功", "service": service_dict}


@router.put("/{service_id}", response_model=dict)
async def update_service(
    service_id: str,
    service_update: ServiceUpdate,
    current_user: dict = Depends(get_current_user)
):
    """更新服务（需要管理员权限）"""
    db = get_database()
    
    if not ObjectId.is_valid(service_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的服务ID"
        )
    
    update_data = {k: v for k, v in service_update.model_dump().items() if v is not None}
    
    result = await db.services.update_one(
        {"_id": ObjectId(service_id)},
        {"$set": update_data}
    )
    
    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="服务不存在"
        )
    
    updated_service = await db.services.find_one({"_id": ObjectId(service_id)})
    updated_service["_id"] = str(updated_service["_id"])
    
    return {"message": "服务更新成功", "service": updated_service}


@router.delete("/{service_id}", response_model=MessageResponse)
async def delete_service(service_id: str, current_user: dict = Depends(get_current_user)):
    """删除服务（需要管理员权限）"""
    db = get_database()
    
    if not ObjectId.is_valid(service_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的服务ID"
        )
    
    result = await db.services.delete_one({"_id": ObjectId(service_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="服务不存在"
        )
    
    return MessageResponse(message="服务删除成功")
