import json

from current_task import load_current_task
from result_summary import build_summary
from task_session import save_session


def main():
    task_data = load_current_task()

    if not task_data:
        print("No current task.")
        return

    result = input(
        "\nResult file/path: "
    ).strip()

    if not result:
        print("Result cancelled.")
        return

    summary = build_summary(
        task_data["task"],
        result
    )

    save_session(
        task=task_data["task"],
        tool=task_data["tool"],
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