from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """应用配置"""
    
    # MongoDB配置
    mongodb_uri: str = "mongodb://localhost:27017/snc-blog"
    
    # JWT配置
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 10080  # 7天
    
    # CORS配置
    client_url: str = "http://localhost:3000"
    
    # 服务器配置
    port: int = 5000
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
