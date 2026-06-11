from port_checker import is_port_open
from assistant_menu import (
    open_comfyui,
    open_qwen_tts,
    run_script
)


def execute_tool(tool_info):
    tool_type = tool_info["type"]
    target = tool_info["target"]

    if tool_type == "script":
        run_script(target)

    elif tool_type == "comfyui":

        if is_port_open(8188):
            print("ComfyUI already running.")
            return

        print("Launching ComfyUI...")
        open_comfyui()

    elif tool_type == "tts":

        if is_port_open(7860):
            print("Qwen3-TTS already running.")
            return

        print("Launching Qwen3-TTS...")
        open_qwen_tts()

    else:
        print("Unknown tool type")