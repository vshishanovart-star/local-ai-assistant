import json
import subprocess
import sys
from pathlib import Path

import requests


BASE_DIR = Path(__file__).resolve().parent

def load_config_for_health_check():
    config_path = BASE_DIR / "config.json"

    if not config_path.exists():
        return None

    try:
        return json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def check_python_version():
    print("Python version:")
    print(sys.version)
    print()


def check_project_path():
    print("Project path:")
    print(BASE_DIR)
    print()


def check_required_files():
    required_files = [
        "config.json",
        "README.md",
        "start.py",
        "assistant_menu.py",
        "ai_memory_chat.py",
        "read_file_ai.py",
        "project_overview_ai.py",
        "config_loader.py",
        "ollama_client.py",
        "logger.py",
        "requirements.txt",
    ]

    print("Required files:")

    for file_name in required_files:
        file_path = BASE_DIR / file_name

        if file_path.exists():
            print(f"[OK]      {file_name}")
        else:
            print(f"[MISSING] {file_name}")

    print()


def check_config():
    config_path = BASE_DIR / "config.json"

    print("Config file:")

    if not config_path.exists():
        print("[MISSING] config.json")
        print()
        return

    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        print("[ERROR] config.json is not valid JSON.")
        print(f"Details: {error}")
        print()
        return

    print("[OK]      config.json is valid JSON.")

    required_keys = [
        "url",
        "model",
        "system_prompt",
        "log_file",
    ]

    for key in required_keys:
        if key in config:
            print(f"[OK]      {key}")
        else:
            print(f"[MISSING] {key}")

    print()


def check_required_dirs():
    required_dirs = [
        "logs",
    ]

    print("Required directories:")

    for dir_name in required_dirs:
        dir_path = BASE_DIR / dir_name

        if dir_path.exists() and dir_path.is_dir():
            print(f"[OK]      {dir_name}")
        else:
            print(f"[MISSING] {dir_name}")

    print()


def check_ollama_api():
    print("Ollama API:")

    config = load_config_for_health_check()

    if config is None:
        print("[SKIPPED] Cannot load config.json.")
        print()
        return

    url = config.get("url")
    model = config.get("model")

    if not url or not model:
        print("[SKIPPED] Missing url or model in config.json.")
        print()
        return

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": "ping"}
        ],
        "stream": False,
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
    except requests.RequestException as error:
        print("[ERROR] Ollama API is not available.")
        print(f"Details: {error}")
        print()
        return

    if response.status_code != 200:
        print(f"[ERROR] Ollama API returned status code {response.status_code}.")
        print(response.text[:300])
        print()
        return

    print("[OK]      Ollama API is available.")
    print()


def check_git_status():
    print("Git status:")

    result = subprocess.run(
        ["git", "status", "--short"],
        cwd=BASE_DIR,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("[ERROR] Git status failed.")
        print(result.stderr.strip())
        print()
        return

    output = result.stdout.strip()

    if not output:
        print("[OK] Working tree clean.")
    else:
        print("[WARNING] Working tree has changes:")
        print(output)

    print()


def main():
    print("Local AI Assistant Health Check")
    print("=" * 32)
    print()

    check_project_path()
    check_python_version()
    check_required_files()
    check_config()
    check_required_dirs()
    check_ollama_api()
    check_git_status()

    print("Health check finished.")


if __name__ == "__main__":
    main()