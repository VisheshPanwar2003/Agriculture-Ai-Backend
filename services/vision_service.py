# services/vision_service.py

import google.generativeai as genai
from services.gemini_service import MODEL_NAME


def analyze_image_question(image, question):
    """
    Analyze a PIL Image using Gemini Vision
    """

    try:
        # Create Gemini model
        model = genai.GenerativeModel(MODEL_NAME)

        # Send image + prompt to Gemini
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
