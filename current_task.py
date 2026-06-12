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
    

def update_current_task(result=None, summary=None, status=None):

    task = load_current_task()

    if not task:
        return

    if result is not None:
        task["result"] = result

    if summary is not None:
        task["summary"] = summary

    if status is not None:
        task["status"] = status

    CURRENT_TASK_FILE.write_text(
        json.dumps(
            task,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )