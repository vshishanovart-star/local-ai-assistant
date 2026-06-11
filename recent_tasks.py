from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TASKS_DIR = BASE_DIR / "output" / "tasks"


def main():
    if not TASKS_DIR.exists():
        print("No task history found.")
        return

    files = sorted(
        TASKS_DIR.glob("*.txt"),
        key=lambda item: item.stat().st_mtime,
        reverse=True
    )

    if not files:
        print("No tasks found.")
        return

    print("\nRecent tasks:\n")

    for file_path in files[:10]:
        content = file_path.read_text(
            encoding="utf-8"
        )

        lines = content.splitlines()

        task_line = lines[0]
        tool_line = lines[2]

        print(f"{task_line} | {tool_line}")

if __name__ == "__main__":
    main()