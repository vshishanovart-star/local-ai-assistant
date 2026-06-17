from qwen_tts_client import generate_speech

result = generate_speech(
    "Привет. Это тест локального AI ассистента."
)

print(result)