from assistant_menu import (
    open_comfyui,
    open_qwen_tts,
    run_script
)
from current_task import load_current_task


def main():
    task = load_current_task()

    if not task:
        print("No active task.")
        return

    print("\nContinue task:\n")

    print(f"Task: {task['task']}")
    print(f"Tool: {task['tool']}")

    print("\nSuggested action:")

    if task["tool"] == "image_generation":
        print("Launching ComfyUI...")
        open_comfyui()

    elif task["tool"] == "tts":
        print("Launching Qwen3-TTS...")
        open_qwen_tts()

    elif task["tool"] == "file_analyzer":
        print("Launching file analyzer...")
        run_script("read_file_ai.py")

    elif task["tool"] == "project_overview":
        print("Launching project overview...")
        run_script("project_overview_ai.py")

    elif task["tool"] == "chat":
        print("Launching AI chat...")
        run_script("ai_memory_chat.py")

if __name__ == "__main__":
    main()