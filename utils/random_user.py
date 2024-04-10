import requests


def get_random_user():
    random_user = requests.get("https://randomuser.me/api/")
    return random_user.json()["results"]
