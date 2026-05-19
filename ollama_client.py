import requests


def ask_ollama(url, model, messages, timeout=120):
    payload = {
        "model": model,
        "messages": messages,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=timeout)
        response.raise_for_status()

        data = response.json()

        return data["message"]["content"]

    except requests.exceptions.ConnectionError:
        return "Ошибка: не удалось подключиться к Ollama. Проверь, запущен ли Ollama."

    except requests.exceptions.Timeout:
        return "Ошибка: Ollama слишком долго не отвечает."

    except requests.exceptions.HTTPError as error:
        return f"Ошибка HTTP: {error}"

    except KeyError:
        return "Ошибка: неожиданный формат ответа от Ollama."

    except Exception as error:
        return f"Неизвестная ошибка: {error}"