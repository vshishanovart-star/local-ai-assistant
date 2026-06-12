from task_history import save_task
from config_loader import load_config
from ollama_client import ask_ollama
from task_prompt_builder import build_prompt
from session_memory import find_similar_tasks
from prompt_storage import save_prompt
from tool_registry import TOOLS
from tool_executor import execute_tool
from current_task import save_current_task


def main():
    config = load_config()

    task = input("\nDescribe task: ").strip()

    if not task:
        print("Task cancelled.")
        return

    similar_tasks = find_similar_tasks(task)

    use_memory = False
    tool = None
    previous_prompt = None

    if similar_tasks:
        print("\nSimilar tasks found:\n")

        for item in similar_tasks[:3]:
            print(f"- {item['task']}")
            print(f"  Tool: {item['tool']}")
            print(f"  Summary: {item['summary']}")
            print()

        answer = input(
            "Reuse previous successful tool? (y/n): "
        ).strip().lower()

        if answer == "y":
            use_memory = True

            tool = similar_tasks[0]["tool"]

            previous_prompt = (
                similar_tasks[0]
                .get("prompt", "")
            )

            print(
                f"\nUsing remembered tool: {tool}"
            )

            if previous_prompt:
                print(
                    "\nPrevious successful prompt found."
                )

    if tool is None:

        tools_text = ""

        for tool_name, info in TOOLS.items():
            tools_text += (
                f"{tool_name}\n"
                f"{info['description']}\n\n"
            )

        router_prompt = f"""
Определи какой инструмент лучше всего подходит.

Доступные инструменты:

{tools_text}

Правила:
- Отвечай только названием инструмента.
- Не объясняй решение.
- Не добавляй комментарии.
- Используй только один инструмент из списка.

Задача:
{task}
"""

        messages = [
            {
                "role": "user",
                "content": router_prompt
            }
        ]

        result = ask_ollama(
            config["url"],
            config["model"],
            messages
        )

        tool = result.strip().lower()

    if use_memory:
        memory_summary = similar_tasks[0]["summary"]

        task_for_prompt = (
            f"{task}\n\n"
            f"Previous experience:\n"
            f"{memory_summary}"
        )
    else:
        task_for_prompt = task

    prompt = build_prompt(
        task_for_prompt,
        tool,
        previous_prompt
    )

    save_prompt(
        task,
        tool,
        prompt
    )

    print("\nGenerated prompt:")
    print(prompt)

    print("\nSelected tool:")
    print(tool)

    save_current_task(task, tool)

    save_task(task, tool)

    tool_info = TOOLS.get(tool)

    if not tool_info:
        print("Unknown tool selected")
        return

    result = execute_tool(
        tool_info,
        prompt
    )

    if result:
        print("\nResult:")
        print(result)

if __name__ == "__main__":
    main()