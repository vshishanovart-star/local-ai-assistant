from current_task import (
    load_current_task,
    update_current_task
)

from result_summary import build_summary
from task_session import save_session


def auto_complete(result_path):

    task_data = load_current_task()

    if not task_data:
        return

    summary = build_summary(
        task_data["task"],
        result_path
    )

    save_session(
        task=task_data["task"],
        tool=task_data["tool"],
        prompt="",
        result=result_path,
        summary=summary,
        success=True
    )

    update_current_task(
        result=result_path,
        summary=summary,
        status="completed"
    )

    return summary