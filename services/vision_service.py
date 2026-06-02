# services/vision_service.py

import google.generativeai as genai
from services.gemini_service import MODEL_NAME


def analyze_image_question(image, question):
    """
    Analyze a PIL image using Gemini Vision
    """

    try:
        model = genai.GenerativeModel(MODEL_NAME)

        response = model.generate_content(
            [
                question,
                image
            ]
        )

        if hasattr(response, "text"):
            return response.text

        return str(response)

    except Exception as e:
        print(f"GEMINI FAILED: {e}")
        raise
