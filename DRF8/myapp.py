import requests
import json

URL = "http://localhost:8000/api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# get_data(1)  # read only data of student where id = 1
# get_data()  # read all data


def post_data():
    data = {
        'name': 'Rahul',
        'roll': 106,
        'city': 'Jaipur'
    }

    headers = {'content-Type': 'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# post_data()

def update_data():
    data = {
        'id': 4,
        'name': 'Dugu',
        'roll': 104,
        'city': 'Jaipur'
    }
    headers = {"content-Type":"application/json"}
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# update_data()


def delete_data():
    data = {'id': 4 }
    headers = {"content-Type":"application/json"}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


delete_data()
