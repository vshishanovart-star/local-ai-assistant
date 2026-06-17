from config_loader import load_config
from ollama_client import ask_ollama
from qwen_tts_client import generate_speech


config = load_config()

messages = [
    {
        "role": "system",
        "content": config["system_prompt"]
    }
]


def ask_chat(question):

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    answer = ask_ollama(
        config["url"],
        config["model"],
        messages
    )

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
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