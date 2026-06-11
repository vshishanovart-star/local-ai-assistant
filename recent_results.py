from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "output" / "task_results"


def main():
    if not RESULTS_DIR.exists():
        print("No task results.")
        return

    files = sorted(
        RESULTS_DIR.glob("*.txt"),
        key=lambda item: item.stat().st_mtime,
        reverse=True
    )

    if not files:
        print("No task results.")
        return

    print("\nRecent results:\n")

    for file_path in files[:10]:
        lines = file_path.read_text(
            encoding="utf-8"
        ).splitlines()

        task = ""
        result = ""

        for line in lines:
            if line.startswith("Task:"):
                task = line.replace("Task:", "").strip()

            if line.startswith("Result:"):
                result = line.replace("Result:", "").strip()

        print(f"Task: {task}")
        print(f"Result: {result}")
        print()


if __name__ == "__main__":
    main()