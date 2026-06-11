from config_loader import load_config
from ollama_client import ask_ollama


def main():
    config = load_config()

    task = input("\nDescribe task: ").strip()

    if not task:
        print("Task cancelled.")
        return

    prompt = f"""
Определи какой инструмент нужен для задачи.

Доступные варианты:

chat
file_analyzer
image_generation
tts

Правила:
- Отвечай только одним словом.
- Не объясняй решение.
- Не добавляй комментарии.
- Используй только один вариант из списка.

Задача:
{task}
"""

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    result = ask_ollama(
        config["url"],
        config["model"],
        messages
    )

    tool = result.strip().lower()

    print("\nSelected tool:")
    print(tool)

    if tool == "tts":
        print("Launch Qwen3-TTS")

    elif tool == "image_generation":
        print("Launch ComfyUI")

    elif tool == "file_analyzer":
        print("Launch File Analyzer")

    elif tool == "chat":
        print("Launch Chat")

    else:
        print("Unknown tool selected")


if __name__ == "__main__":
    main()