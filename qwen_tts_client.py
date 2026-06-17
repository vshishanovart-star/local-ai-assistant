import json
import time
import requests


QWEN_URL = "http://127.0.0.1:7860"


def generate_speech(text):

    payload = {
        "text": text,
        "language": "Русский",
        "voice_description": "Calm male voice, deep and natural",
        "model_size": "1.7B",
        "max_tokens": 1024,
        "temperature": 0.7,
        "top_p": 0.8
    }

    response = requests.post(
        f"{QWEN_URL}/gradio_api/call/v2/generate_voice_design",
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    event_id = response.json()["event_id"]

    stream = requests.get(
        f"{QWEN_URL}/gradio_api/call/generate_voice_design/{event_id}",
        stream=True,
        timeout=300
    )

    audio_path = None

    for line in stream.iter_lines():

        if not line:
            continue

        line = line.decode(
            "utf-8",
            errors="ignore"
        )

        if '"path":' in line:

            try:

                start = line.index('"path": "') + 9
                end = line.index('"', start)

                audio_path = line[start:end]

            except Exception:
                pass

    return audio_path