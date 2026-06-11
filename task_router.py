from task_history import save_task
from config_loader import load_config
from ollama_client import ask_ollama
from tool_registry import TOOLS
from current_task import save_current_task
from assistant_menu import (
    open_comfyui,
    open_qwen_tts,
    run_script
)


def main():
    config = load_config()

    task = input("\nDescribe task: ").strip()

    if not task:
        print("Task cancelled.")
        return

    tools_text = ""

    for tool_name, info in TOOLS.items():
        tools_text += (
            f"{tool_name}\n"
            f"{info['description']}\n\n"
        )

    prompt = f"""
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
            "content": prompt
        }
    ]

    result = ask_ollama(
        config["url"],
        config["model"],
        messages
    )

    tool = result.strip().lower()

    print("\nSelected tool:")
    print(tool)

    save_current_task(task, tool)

    save_task(task, tool)

    tool_info = TOOLS.get(tool)

    if not tool_info:
        print("Unknown tool selected")
        return

    tool_type = tool_info["type"]
    target = tool_info["target"]

    if tool_type == "script":
        run_script(target)

    elif tool_type == "comfyui":
        open_comfyui()

    elif tool_type == "tts":
        open_qwen_tts()

if __name__ == "__main__":
    main()