import requests

from config_loader import load_config


SERVICES = [
    ("Open WebUI", "http://localhost:3000"),
    ("ComfyUI", "http://127.0.0.1:8188"),
    ("Qwen3-TTS", "http://127.0.0.1:7860"),
]


def check_service(name, url):
    try:
        response = requests.get(url, timeout=3)

        if response.status_code < 500:
            print(f"[OK]      {name}")
        else:
            print(f"[ERROR]   {name}")

    except requests.RequestException:
        print(f"[OFFLINE] {name}")


def check_ollama():
    config = load_config()

    url = config["url"]

    try:
        response = requests.post(
            url,
            json={
                "model": config["model"],
                "messages": [
                    {
                        "role": "user",
                        "content": "ping"
                    }
                ],
                "stream": False,
            },
            timeout=5,
        )

        if response.status_code == 200:
            print("[OK]      Ollama")
        else:
            print("[ERROR]   Ollama")

    except requests.RequestException:
        print("[OFFLINE] Ollama")


def main():
    config = load_config()

    print("AI ECOSYSTEM STATUS")
    print("=" * 25)
    print()

    check_ollama()

    for name, url in SERVICES:
        check_service(name, url)

    print()
    print(f"Current model: {config['model']}")


if __name__ == "__main__":
    main()