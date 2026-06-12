from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent
SESSIONS_DIR = BASE_DIR / "output" / "sessions"


def find_similar_tasks(query):
    if not SESSIONS_DIR.exists():
        return []

    query = query.lower()

    matches = []

    for file in SESSIONS_DIR.glob("*.json"):
        try:
            data = json.loads(
                file.read_text(encoding="utf-8")
            )

            if not data.get("success", False):
                continue

            task = data.get("task", "")

            if query in task.lower():
                matches.append(data)

        except Exception:
            pass

    return matches


if __name__ == "__main__":
    results = find_similar_tasks("логотип")

    print(f"Found: {len(results)}")

    for item in results:
        print(item.get("task"))