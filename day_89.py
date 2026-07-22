import requests
respons = requests.get("https://api.github.com/users/octocat")
data=respons.json()
print(data)
print(data["followers"])
print(["public_repos"])
