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


def get_tool_experience():
    stats = {}

    if not SESSIONS_DIR.exists():
        return stats

    for file in SESSIONS_DIR.glob("*.json"):
        try:
            data = json.loads(
                file.read_text(encoding="utf-8")
            )

            if not data.get("success"):
                continue

            tool = data.get("tool")

            stats[tool] = (
                stats.get(tool, 0) + 1
            )

        except Exception:
            pass

    return stats


if __name__ == "__main__":
    print(get_tool_experience())