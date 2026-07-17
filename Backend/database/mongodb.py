import os

from motor.motor_asyncio import (
    AsyncIOMotorClient
)

from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv(
    "MONGODB_URL"
)

DATABASE_NAME = os.getenv(
    "DATABASE_NAME"
)

client = AsyncIOMotorClient(
    MONGODB_URL
)

db = client[DATABASE_NAME]

# COLLECTIONS
users_collection = db["users"]

analysis_collection = db["analysis_history"]

vision_collection = db["vision_history"]

chat_collection = db["chat_history"]