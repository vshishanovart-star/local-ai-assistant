import requests

username = input("GitHub username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    print("\nName:", data["name"])
    print("Bio:", data["bio"])
    print("Public repos:", data["public_repos"])

else:
    print("User not found")