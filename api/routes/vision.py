from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

from PIL import Image

from services.vision_service import (
    analyze_image_question
)

router = APIRouter(
    prefix="/vision",
    tags=["Vision"]
)

@router.post("/analyze")

async def analyze_vision(
    file: UploadFile = File(...),
    question: str = Form("")
):

    try:

        image = Image.open(file.file)

        # DEFAULT QUESTION
        if not question:

            question = """
            Analyze this crop or plant image in detail.
            Detect diseases, health issues,
            severity, and recommendations.
            """

        response = analyze_image_question(
            image,
            question
        )

        return {
            "response": response
        }

    except Exception as e:

        return {
            "error": str(e)
        }