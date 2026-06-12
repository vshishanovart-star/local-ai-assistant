from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent
SESSIONS_DIR = BASE_DIR / "output" / "sessions"


def get_memory_stats():
    total = 0
    successful = 0

    if not SESSIONS_DIR.exists():
        return total, successful

    for file in SESSIONS_DIR.glob("*.json"):
        try:
            data = json.loads(
                file.read_text(encoding="utf-8")
            )

            total += 1

            if data.get("success", False):
                successful += 1

        except Exception:
            pass

    return total, successful


if __name__ == "__main__":
    total, successful = get_memory_stats()

    print(f"Total memories: {total}")
    print(f"Successful memories: {successful}")