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
            Analyze this crop image.
        
            Return ONLY valid JSON in this format:
        
            {
              "crop_name": "",
              "health_status": "",
              "confidence": "",
              "disease_detected": "",
              "severity": "",
              "symptoms": [],
              "recommendations": [],
              "fertilizer_suggestions": [],
              "risk_level": "",
              "summary": ""
            }
        
            Do not return markdown.
            Do not return explanations.
            Return JSON only.
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
