from port_checker import is_port_open


def is_tool_ready(tool_name):
    if tool_name == "image_generation":
        return is_port_open(8188)

    if tool_name == "tts":
        return is_port_open(7860)

    return True