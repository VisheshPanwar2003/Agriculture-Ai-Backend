# services/vision_service.py

import google.generativeai as genai
from PIL import Image
import io

from services.gemini_service import MODEL_NAME


def analyze_image_question(image_file, question):
    """
    Analyze an uploaded image using Gemini Vision
    """

    try:
        # Create model instance
        model = genai.GenerativeModel(MODEL_NAME)

        # Convert uploaded file to PIL Image
        image_bytes = image_file.file.read()

        image = Image.open(
            io.BytesIO(image_bytes)
        )

        # Gemini Vision request
        response = model.generate_content(
            [
                question,
                image
            ]
        )

        return response.text

    except Exception as e:
        print(f"GEMINI FAILED: {str(e)}")
        raise Exception(str(e))
