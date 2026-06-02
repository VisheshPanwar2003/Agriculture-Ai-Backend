# services/vision_service.py

import json
import google.generativeai as genai
from services.gemini_service import MODEL_NAME


def analyze_image_question(image, question):

    try:

        model = genai.GenerativeModel(
            MODEL_NAME
        )

        response = model.generate_content(
            [
                question,
                image
            ]
        )

        result = response.text

        # Remove markdown wrappers if Gemini adds them
        result = result.replace(
            "```json",
            ""
        )

        result = result.replace(
            "```",
            ""
        )

        result = result.strip()

        try:

            return json.loads(result)

        except Exception:

            return {
                "crop_name": "Unknown",
                "health_status": "Unknown",
                "confidence": "N/A",
                "disease_detected": "Not detected",
                "severity": "Unknown",
                "symptoms": [],
                "recommendations": [],
                "fertilizer_suggestions": [],
                "risk_level": "Unknown",
                "summary": result
            }

    except Exception as e:

        print(f"GEMINI FAILED: {e}")
        raise
