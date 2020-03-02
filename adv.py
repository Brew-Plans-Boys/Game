from flask import Flask, jsonify, request
import requests
import json
import sys

INITIALIZE_URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/init/"
MOVEMENT_URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/"


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


visited = {}


# app = Flask(__name__)


# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         node = sys.argv[1]
#     else:
#         node = "http://localhost:5000"


baseUrl = 'https://lambda-treasure-hunt.herokuapp.com'
auth = {"Authorization": "Token 2330ee34073008c724a7066470b88940e7278f5c"}

def init():
    INITIALIZE_URL  = '/api/adv/init/'
    data = requests.get(baseUrl + INITIALIZE_URL, headers=auth)

    if data != None:
        return data.text, 200
    else:
        return ({
            'Error': 'No data returned.'
        })

def move():
    MOVEMENT_URL  = '/api/adv/move/'
    direction = input("Cardinal Direction(N, E, S, W): ").strip()
    directionData = {'direction': direction}
    data = requests.post(baseUrl + MOVEMENT_URL, headers=auth, json=directionData)

    if data != None:
        return data.text, 200
    else:
        return ({
            'Error': 'No data returned.'
        })

print(move())

# r = requests.get(url=node + "/api/adv/init/", json=get_data)

# print(r.json())

# # data = json.dumps(r)

# # print(data)
