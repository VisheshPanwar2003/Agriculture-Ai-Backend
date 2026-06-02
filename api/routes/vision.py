from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    HTTPException
)

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

        with Image.open(file.file) as image:

            # DEFAULT QUESTION
            if not question.strip():

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

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
