from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent
SESSIONS_DIR = BASE_DIR / "output" / "sessions"


def main():

    if not SESSIONS_DIR.exists():
        print("No sessions found.")
        return

    files = sorted(
        SESSIONS_DIR.glob("*.json"),
        reverse=True
    )

    print("\nRecent sessions:\n")

    for index, file in enumerate(files[:10], start=1):

        try:
            data = json.loads(
                file.read_text(
                    encoding="utf-8"
                )
            )

            print(
                f"{index}. {data['task']}"
            )

            print(
                f"   {data['tool']}"
            )

            status = (
                "completed"
                if data.get("success")
                else "failed"
            )

            print(
                f"   {status}"
            )

            print()

        except Exception:
            pass


if __name__ == "__main__":
    main()