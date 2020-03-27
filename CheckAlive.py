import requests


def request(url):
    try:
        return requests.get(url, timeout=5)
    except Exception:
        pass


with open("url.txt", "r") as listfile:
    for i in listfile:
        word = i.strip()
        response = request(word)
        if response:
            print("website is live  " + word)
        else:
            print("website seems down  " + word)
