from fastapi import APIRouter, HTTPException, status, Depends, Query
from bson import ObjectId
from typing import List, Optional
from datetime import datetime
from ..schemas import (
    EventCreate, EventUpdate, EventResponse, MessageResponse
)
from ..core.database import get_database
from ..middleware.auth import get_current_user

router = APIRouter()


@router.get("/", response_model=List[EventResponse])
async def get_events(
    category: Optional[str] = Query(None),
    status_filter: Optional[str] = Query(None, alias="status"),
    published: Optional[str] = Query("true")
):
    """获取所有活动（公开接口）"""
    db = get_database()
    query = {}
    
    if published == "true":
        query["published"] = True
    
    if category and category != "全部":
        query["category"] = category
    
    if status_filter:
        query["status"] = status_filter
    
    events = await db.events.find(query).sort("date", -1).to_list(None)
    
    for event in events:
        event["_id"] = str(event["_id"])
    
    return events


@router.get("/{event_id}", response_model=EventResponse)
async def get_event(event_id: str):
    """获取单个活动（公开接口）"""
    db = get_database()
    
    if not ObjectId.is_valid(event_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的活动ID"
        )
    
    event = await db.events.find_one({"_id": ObjectId(event_id)})
    
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="活动不存在"
        )
    
    event["_id"] = str(event["_id"])
    return event


@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_event(event: EventCreate, current_user: dict = Depends(get_current_user)):
    """创建活动（需要管理员权限）"""
    db = get_database()
    
    event_dict = event.model_dump()
    event_dict["created_at"] = datetime.now()
    
    result = await db.events.insert_one(event_dict)
    
    event_dict["_id"] = str(result.inserted_id)
    
    return {"message": "活动创建成功", "event": event_dict}


@router.put("/{event_id}", response_model=dict)
async def update_event(
    event_id: str,
    event_update: EventUpdate,
    current_user: dict = Depends(get_current_user)
):
    """更新活动（需要管理员权限）"""
    db = get_database()
    
    if not ObjectId.is_valid(event_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的活动ID"
        )
    
    update_data = {k: v for k, v in event_update.model_dump().items() if v is not None}
    
    result = await db.events.update_one(
        {"_id": ObjectId(event_id)},
        {"$set": update_data}
    )
    
    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="活动不存在"
        )
    
    updated_event = await db.events.find_one({"_id": ObjectId(event_id)})
    updated_event["_id"] = str(updated_event["_id"])
    
    return {"message": "活动更新成功", "event": updated_event}


@router.delete("/{event_id}", response_model=MessageResponse)
async def delete_event(event_id: str, current_user: dict = Depends(get_current_user)):
    """删除活动（需要管理员权限）"""
    db = get_database()
    
    if not ObjectId.is_valid(event_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="无效的活动ID"
        )
    
    result = await db.events.delete_one({"_id": ObjectId(event_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="活动不存在"
        )
    
    return MessageResponse(message="活动删除成功")
