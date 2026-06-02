import os

import google.generativeai as genai


genai.configure(

    api_key=os.getenv(
        "GEMINI_API_KEY"
    )

)


model = genai.GenerativeModel(

    "gemini-2.5-flash"

)


def analyze_image_question(

    image,

    question

):

    try:

        response = model.generate_content([

            question,

            image

        ])


        if not response:

            return "No response generated."


        if hasattr(

            response,

            "text"

        ):

            return response.text


        return str(response)

    except Exception as e:

        print(

            "GEMINI ERROR:",

            e

        )

        raise Exception(

            f"Vision analysis failed: {e}"

        )
