import requests

response = requests.get("https://api.github.com")

# print(response.status_code)
# print(response.json())

data = response.json()

print(data["current_user_url"])