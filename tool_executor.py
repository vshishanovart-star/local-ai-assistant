from port_checker import (
    is_port_open,
    wait_for_port
)
from assistant_menu import (
    open_comfyui,
    open_qwen_tts,
    run_script
)

from comfyui_client import generate_image


def execute_tool(tool_info, prompt=None):
    tool_type = tool_info["type"]
    target = tool_info["target"]

    if tool_type == "script":
        run_script(target)

    elif tool_type == "comfyui":

        if not is_port_open(8188):

            print("Launching ComfyUI...")
            open_comfyui()

            print("Waiting for ComfyUI...")

            if not wait_for_port(8188):
                print("ComfyUI startup timeout.")
                return

            print("ComfyUI ready.")

        if not prompt:
            print("Prompt not provided.")
            return

        print("Sending task to ComfyUI...")

        result = generate_image(prompt)

        print("\nComfyUI response:")
        print(result)

    elif tool_type == "tts":

        if is_port_open(7860):
            print("Qwen3-TTS already running.")
            return

        print("Launching Qwen3-TTS...")
        open_qwen_tts()

    else:
        print("Unknown tool type")