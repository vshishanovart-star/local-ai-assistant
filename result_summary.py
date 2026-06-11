from config_loader import load_config
from ollama_client import ask_ollama


def build_summary(task, result):
    config = load_config()

    prompt = f"""
Кратко опиши результат выполнения задачи.

Задача:
{task}

Результат:
{result}

Верни краткое резюме в 1-2 предложениях.
"""

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    summary = ask_ollama(
        config["url"],
        config["model"],
        messages
    )

    return summary.strip()


if __name__ == "__main__":
    result = build_summary(
        "Создай логотип для Kwork",
        "output/kwork_logo.png"
    )

    print(result)