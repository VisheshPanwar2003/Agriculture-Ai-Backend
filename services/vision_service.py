def analyze_image_question(
    image,
    question
):

    try:

        response = model.generate_content([
            question,
            image
        ])

        print(response)

        return response.text

    except Exception as e:

        print(
            "GEMINI FAILED:",
            str(e)
        )

        raise e
