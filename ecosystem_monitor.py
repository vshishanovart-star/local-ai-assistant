from port_checker import is_port_open


def main():
    print("\nAI Ecosystem Status\n")

    print(
        f"Open WebUI: {'Running' if is_port_open(3000) else 'Stopped'}"
    )

    print(
        f"ComfyUI: {'Running' if is_port_open(8188) else 'Stopped'}"
    )

    print(
        f"Qwen3-TTS: {'Running' if is_port_open(7860) else 'Stopped'}"
    )


if __name__ == "__main__":
    main()