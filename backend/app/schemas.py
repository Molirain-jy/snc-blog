from typing import Optional, List, Any
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId


class PyObjectId(ObjectId):
    """自定义ObjectId用于Pydantic"""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


# Blog Schemas
class BlogBase(BaseModel):
    title: str
    excerpt: str
    content: str
    author: str
    date: datetime = Field(default_factory=datetime.now)
    read_time: str = "5 分钟"
    category: str
    tags: List[str] = []
    cover: str = ""
    published: bool = True


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BaseModel):
    title: Optional[str] = None
    excerpt: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    date: Optional[datetime] = None
    read_time: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    cover: Optional[str] = None
    published: Optional[bool] = None


class BlogInDB(BlogBase):
    id: str = Field(alias="_id")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class BlogResponse(BlogInDB):
    pass


# Admin Schemas
class AdminBase(BaseModel):
    username: str
    email: EmailStr


class AdminCreate(AdminBase):
    password: str


class AdminLogin(BaseModel):
    username: str
    password: str


class AdminInDB(AdminBase):
    id: str = Field(alias="_id")
    hashed_password: str
    is_first_login: bool = True
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class AdminResponse(AdminBase):
    id: str


class TokenResponse(BaseModel):
    message: str
    token: str
    admin: AdminResponse


# Service Schemas
class ServiceBase(BaseModel):
    name: str
    description: str
    url: str
    icon: str = "🔗"
    category: str
    order: int = 0
    active: bool = True


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    icon: Optional[str] = None
    category: Optional[str] = None
    order: Optional[int] = None
    active: Optional[bool] = None


class ServiceInDB(ServiceBase):
    id: str = Field(alias="_id")
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ServiceResponse(ServiceInDB):
    pass


# Event Schemas
class EventBase(BaseModel):
    title: str
    description: str
    date: datetime
    location: str = ""
    category: str
    organizer: str = ""
    status: str = "upcoming"
    max_participants: int = 0
    registration_url: str = ""
    published: bool = True


class EventCreate(EventBase):
    pass


class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    location: Optional[str] = None
    category: Optional[str] = None
    organizer: Optional[str] = None
    status: Optional[str] = None
    max_participants: Optional[int] = None
    registration_url: Optional[str] = None
    published: Optional[bool] = None


class EventInDB(EventBase):
    id: str = Field(alias="_id")
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class EventResponse(EventInDB):
    pass


# Settings Schemas
class SettingsBase(BaseModel):
    key: str
    value: Any
    description: str = ""


class SettingsCreate(SettingsBase):
    pass


class SettingsUpdate(BaseModel):
    value: Any
    description: Optional[str] = None


class SettingsInDB(SettingsBase):
    id: str = Field(alias="_id")
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class SettingsResponse(SettingsInDB):
    pass


# Common Response Schemas
class MessageResponse(BaseModel):
    message: str


class HealthResponse(BaseModel):
    status: str
    timestamp: str
