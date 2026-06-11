import requests
import subprocess

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
    print()

    try:
        result = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=name,memory.total",
                "--format=csv,noheader"
            ],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            gpu_info = result.stdout.strip()
            print(f"GPU: {gpu_info}")

    except Exception:
        pass


if __name__ == "__main__":
    main()