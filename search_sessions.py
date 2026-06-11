from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent
SESSIONS_DIR = BASE_DIR / "output" / "sessions"


def main():
    if not SESSIONS_DIR.exists():
        print("No sessions found.")
        return

    query = input("\nSearch: ").strip().lower()

    if not query:
        return

    found = []

    for file in SESSIONS_DIR.glob("*.json"):
        try:
            data = json.loads(
                file.read_text(encoding="utf-8")
            )

            task = data.get("task", "")

            if query in task.lower():
                found.append(data)

        except Exception:
            pass

    print("\nResults:\n")

    if not found:
        print("Nothing found.")
        return

    for item in found:
        print(f"Task: {item['task']}")
        print(f"Tool: {item['tool']}")
        print(f"Summary: {item['summary']}")
        print("-" * 40)


if __name__ == "__main__":
    main()