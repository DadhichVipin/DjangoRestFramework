import requests

URL = "http://localhost:8000/stuinfo/"  # url of API/ end point of API

getRequest = requests.get(url = URL)  # requesting to the api

data = getRequest.json()  # extracting JSON data

print(data)
