from config_loader import load_config
from ollama_client import ask_ollama
from qwen_tts_client import generate_speech


def ask_chat(question):

    config = load_config()

    messages = [
        {
            "role": "user",
            "content": question
        }
    ]

    answer = ask_ollama(
        config["url"],
        config["model"],
        messages
    )

    tts_text = answer[:1000]

    audio_path = None

    try:

        audio_path = generate_speech(
            tts_text
        )

        print("\nGenerated voice:")
        print(audio_path)

    except Exception as error:

        print("\nTTS error:")
        print(error)

    return {
        "answer": answer,
        "audio": audio_path
    }