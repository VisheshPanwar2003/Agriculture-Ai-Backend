from fastapi import APIRouter
from fastapi import Depends

from services.chatbot_service import (
    chatbot
)

from schemas.chatbot_schema import (
    ChatRequest
)

from services.history.chat_history_service import (

    create_chat,

    save_message,

    get_chat_history,

    get_chat_by_id
)

from auth.get_current_user import (
    get_current_user
)

router = APIRouter(
    prefix="/chatbot",
    tags=["Chatbot"]
)

# CREATE NEW CHAT
@router.post("/new")

async def new_chat(

    current_user = Depends(
        get_current_user
    )
):

    chat_id = await create_chat(

        current_user["user_id"]
    )

    return {
        "chat_id": chat_id
    }


# SEND MESSAGE
@router.post("/chat")

async def chat(
    request: ChatRequest
):

    # SAVE USER MESSAGE
    await save_message(

        request.chat_id,

        "user",

        request.message
    )

    # GEMINI RESPONSE
    response = chatbot.chat(
        request.message
    )

    # SAVE AI RESPONSE
    await save_message(

        request.chat_id,

        "assistant",

        response
    )

    return {
        "response": response
    }


# GET USER CHATS
@router.get("/history")

async def history(

    current_user = Depends(
        get_current_user
    )
):

    return await get_chat_history(

        current_user["user_id"]
    )


# GET SINGLE CHAT
@router.get("/{chat_id}")

async def get_chat(
    chat_id: str
):

    return await get_chat_by_id(
        chat_id
    )