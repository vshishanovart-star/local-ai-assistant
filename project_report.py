from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent
SESSIONS_DIR = BASE_DIR / "output" / "sessions"


def main():
    if not SESSIONS_DIR.exists():
        print("No sessions found.")
        return

    sessions = []

    for file in SESSIONS_DIR.glob("*.json"):
        try:
            data = json.loads(
                file.read_text(encoding="utf-8")
            )
            sessions.append(data)

        except Exception:
            pass

    print("\nLOCAL AI ASSISTANT REPORT\n")

    print(f"Total sessions: {len(sessions)}")

    successful = sum(
        1
        for item in sessions
        if item.get("success")
    )

    print(f"Successful: {successful}")

    print("\nTools used:\n")

    stats = {}

    for item in sessions:
        tool = item.get("tool", "unknown")
        stats[tool] = stats.get(tool, 0) + 1

    for tool, count in stats.items():
        print(f"{tool}: {count}")


if __name__ == "__main__":
    main()