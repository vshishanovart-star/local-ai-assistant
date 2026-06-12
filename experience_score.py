from pathlib import Path
import json


BASE_DIR = Path(__file__).resolve().parent
SESSIONS_DIR = BASE_DIR / "output" / "sessions"


def mark_success(task_name):
    for file in SESSIONS_DIR.glob("*.json"):
        try:
            data = json.loads(
                file.read_text(encoding="utf-8")
            )

            if data.get("task") == task_name:
                data["success"] = True

                file.write_text(
                    json.dumps(
                        data,
                        ensure_ascii=False,
                        indent=4
                    ),
                    encoding="utf-8"
                )

                return True

        except Exception:
            pass

    return False


if __name__ == "__main__":
    print(
        mark_success(
            "Создай логотип для Kwork"
        )
    )