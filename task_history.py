from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent
TASKS_DIR = BASE_DIR / "output" / "tasks"


def save_task(task, tool):
    TASKS_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    report = f"""Task: {task}

Tool: {tool}

Time: {timestamp}
"""

    output_file = TASKS_DIR / f"{timestamp}.txt"

    output_file.write_text(
        report,
        encoding="utf-8"
    )


if __name__ == "__main__":
    save_task(
        "Test task",
        "chat"
    )