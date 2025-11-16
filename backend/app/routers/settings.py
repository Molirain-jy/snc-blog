from fastapi import APIRouter, HTTPException, status, Depends
from bson import ObjectId
from typing import Dict, Any
from datetime import datetime
from ..schemas import (
    SettingsCreate, SettingsUpdate, SettingsResponse, MessageResponse
)
from ..core.database import get_database
from ..middleware.auth import get_current_user

router = APIRouter()


@router.get("/", response_model=Dict[str, Any])
async def get_all_settings():
    """获取所有设置（公开接口）"""
    db = get_database()
    
    settings = await db.settings.find().to_list(None)
    
    settings_dict = {}
    for setting in settings:
        settings_dict[setting["key"]] = setting["value"]
    
    return settings_dict


@router.get("/{key}", response_model=Dict[str, Any])
async def get_setting(key: str):
    """获取单个设置（公开接口）"""
    db = get_database()
    
    setting = await db.settings.find_one({"key": key})
    
    if not setting:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="设置不存在"
        )
    
    return {"key": setting["key"], "value": setting["value"]}


@router.post("/", response_model=dict)
async def create_or_update_setting(
    setting: SettingsCreate,
    current_user: dict = Depends(get_current_user)
):
    """创建或更新设置（需要管理员权限）"""
    db = get_database()
    
    existing_setting = await db.settings.find_one({"key": setting.key})
    
    if existing_setting:
        # 更新现有设置
        update_data = {"value": setting.value, "updated_at": datetime.now()}
        if setting.description:
            update_data["description"] = setting.description
        
        await db.settings.update_one(
            {"key": setting.key},
            {"$set": update_data}
        )
        
        updated_setting = await db.settings.find_one({"key": setting.key})
        updated_setting["_id"] = str(updated_setting["_id"])
        
        return {"message": "设置更新成功", "setting": updated_setting}
    else:
        # 创建新设置
        setting_dict = setting.model_dump()
        setting_dict["updated_at"] = datetime.now()
        
        result = await db.settings.insert_one(setting_dict)
        setting_dict["_id"] = str(result.inserted_id)
        
        return {"message": "设置创建成功", "setting": setting_dict}


@router.delete("/{key}", response_model=MessageResponse)
async def delete_setting(key: str, current_user: dict = Depends(get_current_user)):
    """删除设置（需要管理员权限）"""
    db = get_database()
    
    result = await db.settings.delete_one({"key": key})
    
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="设置不存在"
        )
    
    return MessageResponse(message="设置删除成功")
