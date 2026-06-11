from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "output" / "task_results"


def save_result(task, tool, result):
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    output_file = RESULTS_DIR / f"{timestamp}.txt"

    content = f"""Task: {task}

Tool: {tool}

Result: {result}

Time: {timestamp}
"""

    output_file.write_text(content, encoding="utf-8")

    return output_file


def main():
    save_result(
        "Создай логотип для Kwork",
        "image_generation",
        "output/kwork_logo.png"
    )


if __name__ == "__main__":
    main()