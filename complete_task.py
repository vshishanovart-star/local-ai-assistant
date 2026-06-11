import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TASK_FILE = BASE_DIR / "current_task.json"


def main():
    if not TASK_FILE.exists():
        print("No current task.")
        return

    data = json.loads(
        TASK_FILE.read_text(encoding="utf-8")
    )

    data["status"] = "completed"

    TASK_FILE.write_text(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=4
        ),
        encoding="utf-8"
    )

    print("Task completed.")


if __name__ == "__main__":
    main()