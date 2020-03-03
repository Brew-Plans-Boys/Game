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

def checkStatus():
    CHECKSTATUS_URL  = '/api/adv/status/'
    data = requests.post(baseUrl + CHECKSTATUS_URL, headers=auth).json()

    if data != None:
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })

def move():
    MOVEMENT_URL  = '/api/adv/move/'
    direction = input("Cardinal Direction(N, E, S, W): ").strip()
    directionData = {'direction': direction}
    data = requests.post(baseUrl + MOVEMENT_URL, headers=auth, json=directionData).json()

    if data != None:
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })

def carry():
    CARRY_URL  = '/api/adv/carry/'
    carry = input("Type of the name of what you want to drop or carry: ").strip()
    carryData = {'name': carry}
    data = requests.post(baseUrl + CARRY_URL, headers=auth, json=carryData).json()

    if data != None:
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })

def tresurePickup():
    TRESUREPICKUP_URL  = '/api/adv/take/'
    pikcup = input("Type of the name of the tresure you want to pick up or drop: ").strip()
    pikcupData = {'name': pikcup}
    data = requests.post(baseUrl + TRESUREPICKUP_URL, headers=auth, json=pikcupData).json()

    if data != None:
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })

def tresureSell():
    SELL_URL  = '/api/adv/sell/'
    sell = input("Type of the name of the tresure you want to sell: ").strip()
    sellData = {'name': sell}
    data = requests.post(baseUrl + SELL_URL, headers=auth, json=sellData).json()

    if sell is True:
         sellConfirm = input("Are you sure you want to sell this?(Yes/No): ").strip()
         if sellConfirm == 'yes':
             data = requests.post(baseUrl + SELL_URL, headers=auth, json=sellConfirm).json()
         else:
             return "Item not sold" 
    return data

def changeName():
    NAMECHANGE_URL  = '/api/adv/change_name/'
    newName = input("Type your new name: ").strip()
    nameData = {'name': newName}
    data = requests.post(baseUrl + NAMECHANGE_URL, headers=auth, json=nameData).json()

    if data != None:
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })

# print(tresureSell())
# print(tresurePickup())
# print(carry())
# print(changeName())
# print(checkStatus())
# print(move())
# print(init())

# r = requests.get(url=node + "/api/adv/init/", json=get_data)

# print(r.json())

# # data = json.dumps(r)

# # print(data)
