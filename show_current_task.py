from current_task import load_current_task


def main():
    task = load_current_task()

    if not task:
        print("No active task.")
        return

    print("\nCurrent task:\n")

    print(f"Task: {task.get('task', '-')}")
    print(f"Tool: {task.get('tool', '-')}")
    print(f"Status: {task.get('status', '-')}")

    if task.get("result"):
        print(f"Result: {task['result']}")

    if task.get("summary"):
        print(f"Summary: {task['summary']}")


if __name__ == "__main__":
    main()