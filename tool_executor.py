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
        open_comfyui()

    elif tool_type == "tts":
        open_qwen_tts()

    else:
        print("Unknown tool type")