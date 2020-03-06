{
    "proof": 2038104958,
    "difficulty": 6,
    "cooldown": 1.0,
    "messages": [],
    "errors": []
}
import hashlib
import requests
import json
import sys
import datetime
import time
import random

import world
import ast
# Load World


# world = World()

# room_graph = literal_eval(open(room_graph, "r").read())
# world.load_graph(room_graph)

# world.print_rooms()


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


# app = Flask(__name__)
# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         node = sys.argv[1]
#     else:
#         node = "http://localhost:5000"
baseUrl = 'https://lambda-treasure-hunt.herokuapp.com'
colin_auth = {
    "Authorization": "Token 2330ee34073008c724a7066470b88940e7278f5c"}
# eli_auth
auth = {"Authorization": "Token a39b9cc5b11d49d162694cfee69a4710093b2106"}

#pathToCoin = [(w, 0) s 2 e 3 s 9 s 12 e 14 s 34 e 35 s 52 s 68 e 100 s 106 s 111 e 159 w 196 w 197 n 232 (n, 272)]



def init():
    INITIALIZE_URL = '/api/adv/init/'
    data = requests.get(baseUrl + INITIALIZE_URL, headers=auth)
    if data != None:
        print("DATA: ", data.json())
        time.sleep(data.json()['cooldown'])
        return data.json(), 200

    else:
        return ({
            'Error': 'No data returned.'
        })


def checkStatus():
    CHECKSTATUS_URL = '/api/adv/status/'
    data = requests.post(baseUrl + CHECKSTATUS_URL, headers=auth).json()
    if data != None:
        print("Status: ", data)
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })


def move(direction):
    MOVEMENT_URL = '/api/adv/move/'
    # direction = input("Cardinal Direction(N, E, S, W): ").strip()
    directionData = {'direction': direction}
    data = requests.post(baseUrl + MOVEMENT_URL,
                         headers=auth, json=directionData).json()
    time.sleep(data['cooldown'])
    print("Data: ", data)
    if data != None:
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })


def carry():
    CARRY_URL = '/api/adv/carry/'
    carry = input(
        "Type of the name of what you want to drop or carry: ").strip()
    carryData = {'name': carry}
    data = requests.post(baseUrl + CARRY_URL,
                         headers=auth, json=carryData).json()
    if data != None:
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })


def treasurePickup(item_name):
    TREASUREPICKUP_URL = '/api/adv/take/'
    # pikcup = input(
    #     "Type of the name of the tresure you want to pick up or drop: ").strip()
    pickupData = {'name': item_name}
    data = requests.post(baseUrl + TREASUREPICKUP_URL,
                         headers=auth, json=pickupData).json()
    if data != None:
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })


def tresureSell(item_name):
    SELL_URL = '/api/adv/sell/'
    # sell = input("Type of the name of the tresure you want to sell: ").strip()
    sellData = {'name': item_name}
    data = requests.post(baseUrl + SELL_URL, headers=auth,
                         json=sellData).json()
    # if sell is True:
    # sellConfirm = input(
    #         "Are you sure you want to sell this?(Yes/No): ").strip()
    # if sellConfirm == 'yes':
    sellConfirm = {'name': item_name, 'confirm': 'yes'}
    data = requests.post(baseUrl + SELL_URL, headers=auth,
                         json=sellConfirm).json()
    time.sleep(data['cooldown'])
    return data


def changeName():
    NAMECHANGE_URL = '/api/adv/change_name/'
    newName = input("Type your new name: ").strip()
    nameData = {'name': newName}
    data = requests.post(baseUrl + NAMECHANGE_URL,
                         headers=auth, json=nameData).json()
    if data != None:
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })


def lambdaShrineUWU():
    SHRINE_URL = '/api/adv/pray/'
    data = requests.post(baseUrl + SHRINE_URL,
                         headers=auth).json()
    if data != None:
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })


def wiseExplorer(direction, next_room_id):
    MOVEMENT_URL = '/api/adv/move/'
    # direction = input("Cardinal Direction(N, E, S, W): ").strip()
    directionData = {'direction': direction, 'next_room_id': f"{next_room_id}"}
    data = requests.post(baseUrl + MOVEMENT_URL,
                         headers=auth, json=directionData).json()
    time.sleep(data['cooldown'])
    if data != None:
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })


def getLastProof():
    LAST_PROOF_URL = '/api/bc/last_proof'
    data = requests.get(baseUrl + LAST_PROOF_URL, headers=auth).json()
    if data != None:
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })
def mine(hashed_str):
    MINE_URL = '/api/bc/mine'
    postData = {"proof": hashed_str}
    data = requests.post(baseUrl + MINE_URL, headers=auth,json=postData).json()
    if data != None:
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })


checkStatus()

# proof_of_work = (-84756574)
# last_proof = getLastProof()[0]
# last_proof_num = last_proof['proof']
# last_proof_difficulty = last_proof['difficulty']
# hash_str = hashlib.sha256(
#     f"{last_proof_num}{proof_of_work}".encode()).hexdigest()
# dif = ''
# while hash_str[:last_proof_difficulty] != dif.zfill(last_proof_difficulty):
#     proof_of_work += 1
#     print(hash_str)
#     print(hash_str[:last_proof_difficulty])
#     hash_str = hashlib.sha256(
#         f"{last_proof_num}{proof_of_work}".encode()).hexdigest()
# mine(proof_of_work)
