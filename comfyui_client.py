import json
import requests
from pathlib import Path


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

    print("STATUS:", response.status_code)
    print(response.text)

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":

    result = generate_image(
        "professional minimalist logo, vector style"
    )

    print(result)