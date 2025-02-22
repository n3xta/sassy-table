import requests
import json
import tempfile
import os
from playsound import playsound

def generate_speech(text):
    api_key = "sk_762d12664b0bfba01b38598adec0db50504418604a3a0aff"
    voice_id = "x959FyxFeswkQQqFjoPb"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "Content-Type": "application/json",
        "xi-api-key": api_key,
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "speed": 1.15,
            "stability": 0.6,
            "similarity_boost": 0.7,
            "style_exaggeration": 0.1,
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_audio.write(response.content)
            temp_audio_path = temp_audio.name

        playsound(temp_audio_path)
        os.remove(temp_audio_path)
    else:
        print("Error:", response.text)