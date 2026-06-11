from pathlib import Path

from config_loader import load_config
from ollama_client import ask_ollama


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

EXCLUDED_DIRS = {".git", ".venv", "__pycache__", "logs", "output"}
ALLOWED_EXTENSIONS = {".py", ".json", ".md", ".txt"}


def get_project_files():
    files = []

    for path in BASE_DIR.rglob("*"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue

        if path.is_file() and path.suffix in ALLOWED_EXTENSIONS:
            files.append(path)

    return sorted(files, key=lambda item: str(item).lower())


def show_project_files(files):
    print("\nAvailable project files:\n")

    for index, file_path in enumerate(files, start=1):
        print(f"{index}. {file_path.name}")

    print()


def choose_file(files):
    if not files:
        print("No project files found.")
        return None

    show_project_files(files)

    user_input = input("Enter file name or number: ").strip()

    if user_input.isdigit():
        index = int(user_input)

        if 1 <= index <= len(files):
            return files[index - 1]

        print("Invalid file number.")
        return None

    file_path = BASE_DIR / user_input

    if not file_path.exists():
        print("File not found.")
        return None

    if not file_path.is_file():
        print("This is not a file.")
        return None

    return file_path


def choose_mode():
    print("""
Choose mode:
1 - explain
2 - bugs
3 - improve
4 - summary
""")

    mode = input("Enter mode: ").strip()

    if mode == "1":
        return "Объясни содержимое файла простыми словами."

    if mode == "2":
        return "Найди возможные ошибки, слабые места и риски в этом файле. Объясни простыми словами."

    if mode == "3":
        return "Предложи улучшения для этого файла. Объясни, что можно сделать лучше."

    if mode == "4":
        return "Сделай краткое резюме: за что отвечает этот файл и что в нём происходит."

    print("Unknown mode.")
    return None


def save_analysis_result(file_path, task, ai_message):
    OUTPUT_DIR.mkdir(exist_ok=True)

    output_path = OUTPUT_DIR / "last_file_analysis.md"

    report = f"""
# File Analysis Report

## Analyzed file

{file_path.name}

## Task

{task}

## AI result

{ai_message}
"""

    output_path.write_text(report.strip(), encoding="utf-8")

    return output_path


def main():
    config = load_config()

    url = config["url"]
    model = config["model"]

    files = get_project_files()
    file_path = choose_file(files)

    if file_path is None:
        return

    task = choose_mode()

    if task is None:
        return

    content = file_path.read_text(encoding="utf-8")

    prompt = f"""
Ты локальный AI-помощник для анализа файлов проекта.

Задача:
{task}

Имя файла: {file_path.name}

Содержимое файла:

{content}
"""

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    ai_message = ask_ollama(url, model, messages, timeout=120)

    output_path = save_analysis_result(file_path, task, ai_message)

    print("\nAI result:\n")
    print(ai_message)

    print(f"\nSaved to: {output_path.relative_to(BASE_DIR)}")

    input("\nPress Enter to finish...")


if __name__ == "__main__":
    main()
