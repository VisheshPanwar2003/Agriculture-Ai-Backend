from datetime import datetime

import json

from data.crops import CROP_DATA

from services.gemini_service import (
    generate_response
)


class FarmersAlmanac:

    def get_daily_almanac(self):

        today = datetime.now().strftime(
            "%d %B %Y"
        )

        return {
            "date": today,
            "moon_phase": "Waxing Crescent",
            "activity": "Plant leafy vegetables",

            "best_for": [
                "Spinach",
                "Lettuce",
                "Cabbage"
            ]
        }

    def get_seasonal_guide(
        self,
        region
    ):

        return {

            "region": region,

            "Kharif": [
                "Rice",
                "Maize",
                "Cotton"
            ],

            "Rabi": [
                "Wheat",
                "Mustard",
                "Potato"
            ],

            "Summer": [
                "Watermelon",
                "Cucumber",
                "Tomato"
            ]
        }

    def get_crop_ai_data(
        self,
        crop_name
    ):

        crop = CROP_DATA.get(
            crop_name
        )

        if not crop:

            return {
                "error": "Crop not found"
            }

        prompt = f"""
You are an agriculture expert AI.

Crop: {crop_name}

Days to maturity:
{crop["days_to_maturity"]}

Watering:
{crop["watering"]}

Pests:
{", ".join(crop["pests"])}

Companion Plants:
{", ".join(crop["companion_plants"])}

Harvest Time:
{crop["harvest_time"]}

Generate farming insights.

Return ONLY valid JSON.

Format:

{{
    "summary": "short crop overview",

    "recommendations": [
        "tip 1",
        "tip 2",
        "tip 3"
    ]
}}
"""

        try:

            response = generate_response(
                prompt
            )

            # CLEAN RESPONSE
            response = response.replace(
                "```json",
                ""
            )

            response = response.replace(
                "```",
                ""
            )

            ai_data = json.loads(
                response
            )

            return {
                "crop_data": crop,
                "ai_data": ai_data
            }

        except Exception as e:

            print(e)

            return {

                "crop_data": crop,

                "ai_data": {

                    "summary":
                    "AI insights unavailable.",

                    "recommendations": [
                        "Monitor crop regularly",
                        "Maintain proper irrigation",
                        "Check for pest attacks"
                    ]
                }
            }