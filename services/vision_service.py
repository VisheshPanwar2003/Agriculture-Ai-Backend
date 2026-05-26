import google.generativeai as genai

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def analyze_image_question(
    image,
    question
):

    response = model.generate_content([
        question,
        image
    ])

    return response.text