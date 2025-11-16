from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

# MongoDB客户端
client: AsyncIOMotorClient = None

# 数据库
db = None


async def connect_to_mongo():
    """连接到MongoDB"""
    global client, db
    client = AsyncIOMotorClient(settings.mongodb_uri)
    db = client.get_default_database()
    print("✅ MongoDB 连接成功")


async def close_mongo_connection():
    """关闭MongoDB连接"""
    global client
    if client:
        client.close()
        print("❌ MongoDB 连接已关闭")


def get_database():
    """获取数据库实例"""
    return db
