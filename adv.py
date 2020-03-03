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


app = Flask(__name__)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"


@app.route('/api/adv/init/', methods=['GET'])
def init():
    data = request.get_json()

    if data != None:
        return jsonify(data), 200
    else:
        return jsonify({
            'Error': 'No data returned.'
        })
    # response = {
    #     "message": "success"
    # }
    # return jsonify(data), 200


get_data = {"Authorization": "Token 2330ee34073008c724a7066470b88940e7278f5c"}


r = requests.get(url=node + "/api/adv/init/", json=get_data)

data = r.json()

print(data)
