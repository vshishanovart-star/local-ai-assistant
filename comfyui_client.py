import json
import requests
from pathlib import Path

from comfyui_history import wait_for_prompt
from comfyui_result_parser import (
    extract_image_path
)


WORKFLOW_PATH = Path(
    "api_workflow.json"
)

COMFY_URL = "http://127.0.0.1:8188/prompt"


def generate_image(prompt_text):

    workflow = json.loads(
        WORKFLOW_PATH.read_text(
            encoding="utf-8"
        )
    )

    workflow["6"]["inputs"]["text"] = prompt_text

    payload = {
        "prompt": workflow
    }

    response = requests.post(
        COMFY_URL,
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    prompt_id = data["prompt_id"]

    print("\nWaiting for generation...")

    history = wait_for_prompt(prompt_id)

    result_file = extract_image_path(
        history
    )

    print(
        "\nGenerated file:"
    )
    print(result_file)

    return result_file


if __name__ == "__main__":

    result = generate_image(
        "professional minimalist logo, vector style"
    )

    print(result)