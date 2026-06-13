from config_loader import load_config
from ollama_client import ask_ollama


def ask_chat(question):

    config = load_config()

    messages = [
        {
            "role": "user",
            "content": question
        }
    ]

    return ask_ollama(
        config["url"],
        config["model"],
        messages
    )