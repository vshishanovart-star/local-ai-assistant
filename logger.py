from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def write_log(log_file, role, text):
    log_path = BASE_DIR / log_file
    log_path.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_path, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {role}: {text}\n")