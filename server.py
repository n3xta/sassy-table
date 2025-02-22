from flask import Flask, request, jsonify
import openai
from config import OPENAI_API_KEY

app = Flask(__name__)
openai.api_key = OPENAI_API_KEY

def send_to_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

@app.route("/ai_response", methods=["POST"])
def ai_response():
    data = request.json
    prompt = data.get("prompt", "")
    response_text = send_to_ai(prompt)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True, port=5000)