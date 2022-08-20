import json

import requests

URL = "http://localhost:8000/create/"           # for sending request... End point of API

data = {            # JSON Data that we want to insert in
    'name':'NItin',
    'roll':'102',
    'city':'Jaipur'
}

json_data = json.dumps(data)  # convert JSON to Python native using dumps method

r = requests.post(url= URL, data= json_data)  # sending data as request to insert

data = r.json()  # extracting response msg get from api

print(data)

