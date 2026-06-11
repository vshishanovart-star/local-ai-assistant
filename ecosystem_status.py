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


def check_docker():
    try:
        result = subprocess.run(
            ["docker", "ps"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("[OK]      Docker")
        else:
            print("[OFFLINE] Docker")

    except Exception:
        print("[OFFLINE] Docker")


def show_ollama_models():
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return

        lines = result.stdout.strip().splitlines()

        if len(lines) <= 1:
            return

        print()
        print(f"Ollama models: {len(lines) - 1}")

        for line in lines[1:]:
            model_name = line.split()[0]
            print(f" - {model_name}")

    except Exception:
        pass


def main():
    config = load_config()

    print("AI ECOSYSTEM STATUS")
    print("=" * 25)
    print()

    check_ollama()
    check_docker()

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
            
        show_ollama_models()

    except Exception:
        pass


if __name__ == "__main__":
    main()