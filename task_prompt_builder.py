from config_loader import load_config
from ollama_client import ask_ollama


def build_prompt(task, tool):
    if tool == "image_generation":
        instruction = """
Преобразуй задачу пользователя в качественный промпт
для генерации изображения.

Не придумывай факты, которых нет в задаче.

Если задача слишком короткая,
дополни её только общими профессиональными
характеристиками качества изображения.

Например:

"логотип" →
"professional minimalist logo,
vector style,
clean design,
high quality branding"

Не придумывай названия компаний,
цвета или объекты,
если они не указаны пользователем.

Верни только готовый промпт.
"""

    elif tool == "tts":
        instruction = """
Подготовь текст для озвучивания.

Исправь ошибки если они есть.
Верни только итоговый текст.
"""

    else:
        return task

    config = load_config()

    messages = [
        {
            "role": "user",
            "content": f"""
{instruction}

Задача:

{task}
"""
        }
    ]

    result = ask_ollama(
        config["url"],
        config["model"],
        messages
    )

    return result.strip()


if __name__ == "__main__":
    test = build_prompt(
        "Создай логотип для Kwork",
        "image_generation"
    )

    print(test)