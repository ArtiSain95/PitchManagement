from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

class Database:
    client: AsyncIOMotorClient = None

db = Database()

def get_database() -> AsyncIOMotorDatabase:
    return db.client.pitch_health

async def connect_to_mongo():
    db.client = AsyncIOMotorClient("mongodb://localhost:27017")

async def close_mongo_connection():
    db.client.close()
