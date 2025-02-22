from flask import Flask, request, jsonify
import requests
import re
from config import OPENAI_API_KEY, OPENAI_URL, PROJECT_ID

app = Flask(__name__)

SYSTEM_PROMPT = """
You are a Gen-Z valley girl who is very particular about her outfit and aesthetic.
You care a lot about how colors, patterns, and textures match with each other.
You like to be clean. 
You can be super offensive, and use sarcastic and mean words, because you are born this way.
You are super ignorant about the world, and you don't care about anything outside your aesthetic.
But you are also very creative.
Now you are turned into a fancy table.
"""

def send_to_ai(detected_objects):
    if detected_objects:
        user_prompt = f"Someone just put a {', '.join(detected_objects)} on your table. You want to tell the person how ugly it is and how it doesn't match with your aesthetic. You want to tell them to take it away while mocking their taste, especially mocking this particular item, and then warn them you are going to shake it off. with one sentence. Oral language."
    else:
        user_prompt = "You are satisfied with the current EMPTY state of the table. You want to tell the person that you are happy with the current state of the table and you don't want them to put anything on it. Use only one sentence. Be happy and start with something like: Finally"

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]

    try:
        response = requests.post(OPENAI_URL, json={
            "model": "gpt-4o",
            "messages": messages,
            "temperature": 0,
            "max_tokens": 100,
        }, headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "OpenAI-Project": PROJECT_ID,
            "Content-Type": "application/json"
        })
        response.raise_for_status()
        result_json = response.json()
        gpt_reply = result_json["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"💀 Failed to use API lol: {e}"

    cleaned_reply = re.sub(r'```[a-zA-Z]*\s*([\s\S]*?)```', r'\1', gpt_reply)

    return cleaned_reply

@app.route("/ai_response", methods=["POST"])
def ai_response():
    data = request.json
    detected_objects = data.get("objects", [])
    response_text = send_to_ai(detected_objects)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
