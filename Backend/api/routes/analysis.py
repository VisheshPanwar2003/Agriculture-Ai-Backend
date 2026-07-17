from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from PIL import Image

from ai.ai_model import ai_analyzer

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)

@router.post("/predict")

async def predict_crop(
    file: UploadFile = File(...)
):

    image = Image.open(file.file)

    result = ai_analyzer.analyze_image(
        image,
        "crop"
    )

    return result