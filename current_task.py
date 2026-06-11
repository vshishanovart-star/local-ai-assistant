import json
from pathlib import Path


CURRENT_TASK_FILE = Path(__file__).parent / "current_task.json"


def save_current_task(task, tool):
    data = {
        "task": task,
        "tool": tool,
        "status": "active"
    }

    CURRENT_TASK_FILE.write_text(
        json.dumps(data, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )


def load_current_task():
    if not CURRENT_TASK_FILE.exists():
        return None

    try:
        return json.loads(
            CURRENT_TASK_FILE.read_text(encoding="utf-8")
        )

    except Exception:
        return None