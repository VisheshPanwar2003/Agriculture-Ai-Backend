from services.gemini_service import generate_response


class AgricultureAssistant:

    def __init__(self):

        self.history = []

    def chat(self, message):

        # STORE USER MESSAGE
        self.history.append(
            f"User: {message}"
        )

        # KEEP ONLY LAST 6 MESSAGES
        self.history = self.history[-6:]

        conversation = "\n".join(
            self.history
        )

        prompt = f"""
You are AgriSense AI,
an expert agriculture assistant.

You help farmers with:
- crop diseases
- fertilizers
- irrigation
- pesticides
- organic farming
- weather impact
- soil health
- crop recommendations

Previous Conversation:
{conversation}

Reply conversationally and clearly.

Keep responses:
- practical
- concise
- farmer friendly
- well formatted

Current User Message:
{message}
"""

        response = generate_response(
            prompt
        )

        # STORE AI RESPONSE
        self.history.append(
            f"AI: {response}"
        )

        return response


chatbot = AgricultureAssistant()