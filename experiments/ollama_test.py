import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen2.5-coder:7b",
    "prompt": "Explain what Python is in one short sentence.",
    "stream": False
}

response = requests.post(url, json=payload)

data = response.json()

print(data["response"])