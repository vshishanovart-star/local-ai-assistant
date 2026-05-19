from pathlib import Path

from config_loader import load_config
from ollama_client import ask_ollama


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

ALLOWED_EXTENSIONS = [".py", ".json", ".txt", ".gitignore", ".md"]
SKIP_DIRS = [".git", ".venv", "__pycache__", "logs", "output"]


def should_skip(path):
    for part in path.parts:
        if part in SKIP_DIRS:
            return True

    return False


def is_allowed_file(path):
    if path.name == ".gitignore":
        return True

    return path.suffix in ALLOWED_EXTENSIONS


def collect_project_files():
    files_data = []

    for path in BASE_DIR.rglob("*"):
        if should_skip(path):
            continue

        if not path.is_file():
            continue

        if path.name == "README.md":
            continue

        if not is_allowed_file(path):
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        relative_path = path.relative_to(BASE_DIR)

        files_data.append({
            "path": str(relative_path),
            "content": content
        })

    return files_data


def build_project_text(files_data):
    project_text = ""

    for file_info in files_data:
        project_text += f"\n\n--- FILE: {file_info['path']} ---\n"
        project_text += file_info["content"]

    return project_text


def build_file_list_text(files_data):
    file_list_text = ""

    for file_info in files_data:
        file_list_text += f"- {file_info['path']}\n"

    return file_list_text


def build_prompt(file_list_text, project_text):
    return f"""
ОТВЕЧАЙ ТОЛЬКО НА РУССКОМ ЯЗЫКЕ.
Ты локальный AI-помощник для анализа проекта.
Если ты начнёшь отвечать на английском языке, ответ будет считаться неправильным.
Все разделы, пояснения, выводы и советы должны быть только на русском языке.
Английскими могут оставаться только имена файлов, команды, названия функций и фрагменты кода.

Проанализируй проект строго по содержимому файлов ниже.
Проанализируй проект строго по содержимому файлов ниже.

Важные правила:
Язык ответа:
- Весь ответ должен быть только на русском языке.
- Даже если README.md, код, команды или комментарии написаны на английском, объясняй их по-русски.
- Английские названия файлов, команд и кода можно оставлять как есть.
- Не пиши английские объяснения.

Важные правила:
- Не придумывай назначение файлов.
- Не упоминай файлы, которых нет в списке файлов проекта.
- Описывай только то, что явно видно из кода.
- Если назначение файла неясно, так и напиши: "назначение неясно".
- Отделяй рабочие файлы от учебных, тестовых и экспериментальных.
- Не предлагай слишком общие советы.
- Давай конкретные следующие шаги именно для этого проекта.

Список файлов проекта:
{file_list_text}

Сделай ответ по структуре:

Сделай обычный текстовый ответ на русском языке.

Используй ровно такие разделы:

1. Что это за проект
2. Рабочие файлы проекта и их роль
3. Учебные, тестовые или экспериментальные файлы
4. Что уже сделано хорошо
5. Слабые места или риски
6. Один самый логичный следующий шаг

Не отвечай в JSON.
Не пиши кодовый блок.
Не пересказывай README целиком.
Важно: итоговый анализ напиши на русском языке.

Файлы проекта:

{project_text}
"""


def save_project_overview(ai_message):
    OUTPUT_DIR.mkdir(exist_ok=True)

    output_path = OUTPUT_DIR / "last_project_overview.txt"

    report = f"""
Project overview report

AI result:

{ai_message}
"""

    output_path.write_text(report.strip(), encoding="utf-8")

    return output_path


def needs_rewrite(ai_message):
    if "```" in ai_message:
        return True

    forbidden_fragments = [
        "Project Overview",
        "Analysis",
        "What This Project",
        "Key Components",
        "Usage Scenarios",
        "Technical Details",
        "Challenges",
        "Limitations",
        "Future Improvements",
        "Conclusion",
        "Summary",
        "This project",
        "The project",
        "The tool",
        "developers",
        "students",
        "configuration",
        "dependencies",
    ]

    lower_message = ai_message.lower()

    for fragment in forbidden_fragments:
        if fragment.lower() in lower_message:
            return True

    forbidden_chars = [
        "被",
        "的",
        "是",
        "这",
        "を",
        "に",
        "は",
    ]

    for char in forbidden_chars:
        if char in ai_message:
            return True

    required_sections = [
        "1. Что это за проект",
        "2. Рабочие файлы проекта и их роль",
        "3. Учебные, тестовые или экспериментальные файлы",
        "4. Что уже сделано хорошо",
        "5. Слабые места или риски",
        "6. Один самый логичный следующий шаг",
    ]

    for section in required_sections:
        if section not in ai_message:
            return True

    return False


def rewrite_project_overview(url, model, file_list_text, project_text):
    rewrite_prompt = f"""
Сделай новый обзор проекта строго по данным ниже.

ОЧЕНЬ ВАЖНО:
- Не переписывай предыдущий ответ.
- Не используй догадки.
- Не придумывай папки, файлы и назначение файлов.
- Используй только список файлов и содержимое файлов ниже.
- Если файла нет в списке, не упоминай его.
- Ответ должен быть только на русском языке.
- Не используй английский язык для объяснений.
- Английские слова можно оставлять только в именах файлов, командах, функциях и коде.
- Не используй Markdown-кодовые блоки.
- Не пиши JSON.

Список файлов проекта:
{file_list_text}

Используй ровно такие разделы:

1. Что это за проект
2. Рабочие файлы проекта и их роль
3. Учебные, тестовые или экспериментальные файлы
4. Что уже сделано хорошо
5. Слабые места или риски
6. Один самый логичный следующий шаг

Файлы проекта:

{project_text}
"""

    messages = [
        {
            "role": "system",
            "content": (
                "Ты анализируешь проект строго по предоставленным файлам. "
                "Ты не имеешь права придумывать файлы, папки или возможности проекта. "
                "Отвечай только на русском языке."
            )
        },
        {
            "role": "user",
            "content": rewrite_prompt
        }
    ]

    return ask_ollama(url, model, messages, timeout=180)


def main():
    config = load_config()

    url = config["url"]
    model = config["model"]

    files_data = collect_project_files()

    if not files_data:
        print("No project files found.")
        return

    project_text = build_project_text(files_data)
    file_list_text = build_file_list_text(files_data)
    prompt = build_prompt(file_list_text, project_text)

    messages = [
        {
            "role": "system",
            "content": (
                "Ты отвечаешь только на русском языке. "
                "Не используй английский язык для объяснений. "
                "Если в коде есть английские слова, имена файлов или команды, "
                "оставляй их как технические названия, но все пояснения пиши по-русски."
            )
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    ai_message = ask_ollama(url, model, messages, timeout=180)

    if needs_rewrite(ai_message):
        print("\nInitial answer did not match the expected format. Rewriting...\n")
        ai_message = rewrite_project_overview(url, model, file_list_text, project_text)

        if needs_rewrite(ai_message):
            ai_message = """
Не удалось получить корректный обзор проекта от локальной модели.

Причина:
локальная модель не соблюдала нужный формат ответа или добавила неподходящий текст.

Что можно сделать:
1. Повторить анализ позже.
2. Уменьшить количество файлов для анализа.
3. Улучшить промпт для локальной модели.
4. Использовать более сильную локальную модель.

Проект технически работает, но вместо AI-обзора сохранено служебное сообщение.
""".strip()

    output_path = save_project_overview(ai_message)

    print("\nProject overview:\n")
    print(ai_message)

    print(f"\nSaved to: {output_path.relative_to(BASE_DIR)}")

    input("\nPress Enter to finish...")


if __name__ == "__main__":
    main()