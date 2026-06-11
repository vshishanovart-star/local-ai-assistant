from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = BASE_DIR / "output" / "prompts"


def save_prompt(task, tool, prompt):
    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_path = PROMPTS_DIR / f"{timestamp}.txt"

    content = f"""Task: {task}

Tool: {tool}

Prompt:

{prompt}
"""

    file_path.write_text(content, encoding="utf-8")

    return file_path