import json

from current_task import load_current_task
from result_summary import build_summary
from task_session import save_session
from find_latest_result import find_latest_result


def main():
    task_data = load_current_task()

    if not task_data:
        print("No current task.")
        return

    tool = task_data["tool"]

    result_file = find_latest_result(tool)

    if not result_file:
        print("Result not found.")
        return

    result = str(result_file)

    print("\nDetected result:")
    print(result)

    summary = build_summary(
        task_data["task"],
        result
    )

    save_session(
        task=task_data["task"],
        tool=tool,
        prompt="",
        result=result,
        summary=summary,
        success=True
    )

    print("\nSummary:")
    print(summary)

    task_data["status"] = "completed"

    with open(
        "current_task.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            task_data,
            f,
            ensure_ascii=False,
            indent=4
        )

    print("\nTask completed.")
    print("Session saved.")


if __name__ == "__main__":
    main()