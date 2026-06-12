from pathlib import Path
from datetime import datetime
import json


BASE_DIR = Path(__file__).resolve().parent
SESSIONS_DIR = BASE_DIR / "output" / "sessions"


def save_session(
    task,
    tool,
    prompt,
    result,
    summary,
    success=True
):
    SESSIONS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    data = {
        "task": task,
        "tool": tool,
        "prompt": prompt,
        "result": result,
        "summary": summary,
        "time": timestamp,
        "success": success
    }

    file_path = (
        SESSIONS_DIR /
        f"{timestamp}.json"
    )

    file_path.write_text(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=4
        ),
        encoding="utf-8"
    )

    return file_path