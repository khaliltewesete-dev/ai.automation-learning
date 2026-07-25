import requests

username = input("enter your username: ")
url = f"https://api.github.com/users/{username}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # ← أضفنا الأقواس!
    print("name: ", data["name"])
    print("Repos:", data["public_repos"])
    print("Followers:", data["followers"])
else:
    print("user not found")