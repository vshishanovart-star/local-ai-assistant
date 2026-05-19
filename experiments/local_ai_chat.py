import requests

prompt = input("You: ")

url = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen2.5-coder:7b",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=payload)

data = response.json()

print("\nAI:", data["response"])