import json

def parse_ai_json(ai_response: str):

    ai_response = ai_response.replace("None", "null")
    ai_response = ai_response.replace("True", "true")
    ai_response = ai_response.replace("False", "false")

    ai_response = ai_response.strip()

    if not ai_response.endswith("}"):
        ai_response += "\n}"

    return json.loads(ai_response)