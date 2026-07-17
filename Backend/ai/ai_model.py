import json
import re

import google.generativeai as genai

from services.gemini_service import MODEL_NAME


class AgricultureAI:

    def analyze_image(self, img, analysis_type):

        try:

            model = genai.GenerativeModel(
                MODEL_NAME
            )

            prompt = f"""
You are an advanced agriculture AI assistant.

Analyze the uploaded crop or plant image carefully.

Your task:
- Identify crop type
- Detect plant disease if present
- Estimate severity
- Identify visible issues
- Provide actionable recommendations

Return ONLY valid JSON.

Required JSON format:

{{
    "type": "Crop Type",
    "status": "Disease Name or Healthy",
    "severity": "Low | Medium | High",
    "confidence": 0.95,
    "issues": "Short issue summary",

    "recommendations": [
        "recommendation 1",
        "recommendation 2",
        "recommendation 3",
        "recommendation 4"
    ]
}}

Rules:
- confidence must be between 0 and 1
- recommendations must always be an array
- severity must be Low, Medium, or High
- return only JSON
- no markdown
- no explanation outside JSON
"""

            response = model.generate_content(
                [prompt, img]
            )

            text = response.text.strip()

            # REMOVE MARKDOWN
            text = text.replace(
                "```json",
                ""
            )

            text = text.replace(
                "```",
                ""
            )

            # SAFE JSON EXTRACTION
            match = re.search(
                r"\{.*\}",
                text,
                re.DOTALL
            )

            if match:

                text = match.group()

            result = json.loads(text)

            # FALLBACK SAFETY
            result.setdefault(
                "type",
                "Unknown Crop"
            )

            result.setdefault(
                "status",
                "Unknown"
            )

            result.setdefault(
                "severity",
                "Medium"
            )

            result.setdefault(
                "confidence",
                0.75
            )

            result.setdefault(
                "issues",
                "No issues detected"
            )

            result.setdefault(
                "recommendations",
                [
                    "Monitor crop condition regularly"
                ]
            )

            return result

        except Exception as e:

            return {
                "type": "Unknown",
                "status": "Analysis Failed",
                "severity": "Unknown",
                "confidence": 0,
                "issues": str(e),

                "recommendations": [
                    "Try uploading a clearer image",
                    "Ensure plant is properly visible",
                    "Check internet/API connection"
                ]
            }


ai_analyzer = AgricultureAI()