from current_task import load_current_task


def main():
    task = load_current_task()

    if not task:
        print("No active task.")
        return

    print("\nCurrent task:\n")

    print(f"Task: {task['task']}")
    print(f"Tool: {task['tool']}")
    print(f"Status: {task['status']}")


if __name__ == "__main__":
    main()