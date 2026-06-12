import requests
import time


HISTORY_URL = "http://127.0.0.1:8188/history"


def wait_for_prompt(prompt_id, timeout=600):
    start_time = time.time()

    while True:

        response = requests.get(
            HISTORY_URL,
            timeout=30
        )

        response.raise_for_status()

        history = response.json()

        if prompt_id in history:
            return history[prompt_id]

        if time.time() - start_time > timeout:
            raise TimeoutError(
                "Generation timeout."
            )

        time.sleep(2)


if __name__ == "__main__":

    prompt_id = input("Prompt ID: ").strip()

    result = wait_for_prompt(prompt_id)

    print(result)