from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent
SESSIONS_DIR = BASE_DIR / "output" / "sessions"


def calculate_score(query, task):
    query_words = query.lower().split()
    task_words = task.lower().split()

    score = 0

    for word in query_words:
        if word in task_words:
            score += 1

    return score


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

            score = calculate_score(
                query,
                task
            )

            if score > 0:
                found.append(
                    (score, data)
                )

        except Exception:
            pass

    found.sort(
        key=lambda item: item[0],
        reverse=True
    )

    print("\nResults:\n")

    if not found:
        print("Nothing found.")
        return

    for score, item in found[:10]:
        print(f"Score: {score}")
        print(f"Task: {item['task']}")
        print(f"Tool: {item['tool']}")
        print(f"Summary: {item['summary']}")
        print("-" * 40)


if __name__ == "__main__":
    main()