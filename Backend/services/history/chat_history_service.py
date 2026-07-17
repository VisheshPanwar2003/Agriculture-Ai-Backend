from datetime import datetime

from bson import ObjectId

from database.mongodb import (
    chat_collection
)


# CREATE CHAT
async def create_chat(
    user_id
):

    document = {

        "user_id": user_id,

        "messages": [],

        "created_at": datetime.utcnow(),

        "updated_at": datetime.utcnow()
    }

    result = await chat_collection.insert_one(
        document
    )

    return str(result.inserted_id)


# SAVE MESSAGE
async def save_message(

    chat_id,

    role,

    content
):

    await chat_collection.update_one(

        {
            "_id": ObjectId(chat_id)
        },

        {
            "$push": {

                "messages": {

                    "role": role,

                    "content": content
                }
            },

            "$set": {

                "updated_at":
                datetime.utcnow()
            }
        }
    )


# GET USER CHATS
async def get_chat_history(
    user_id
):

    chats = []

    cursor = chat_collection.find(

        {

            "user_id": user_id,

            "messages.0": {
                "$exists": True
            }
        }

    ).sort(
        "updated_at",
        -1
    )

    async for document in cursor:

        document["_id"] = str(
            document["_id"]
        )

        chats.append(document)

    return chats


# GET SINGLE CHAT
async def get_chat_by_id(
    chat_id
):

    document = await chat_collection.find_one(

        {
            "_id": ObjectId(chat_id)
        }
    )

    if not document:

        return None

    document["_id"] = str(
        document["_id"]
    )

    return document