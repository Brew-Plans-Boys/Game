import requests
import json
import sys
import datetime
import time
import hashlib
import world
import ast
# Load World
from dfs import DestinationTraversal


# world = World()

# room_graph = literal_eval(open(room_graph, "r").read())
# world.load_graph(room_graph)

# world.print_rooms()


INITIALIZE_URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/init/"
MOVEMENT_URL = "https://lambda-treasure-hunt.herokuapp.com/api/adv/move/"


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class DestinationTraversal():
    def __init__(self):
        pass

    def dfs(self, all_rooms, starting_room, destination_room, room_ids=None, visited=None,):
        q = Queue()
        if visited == None:
            visited = set()
        if room_ids == None:
            room_ids = [starting_room]
        q.enqueue(room_ids)
        # directions = []

        while q.size() > 0:
            current_room = q.dequeue()

            if current_room == destination_room:
                return room_ids

            if current_room[-1] not in visited:
                visited.add(current_room[-1])

                for item in all_rooms[f"{current_room}"].items():
                    room_ids_copy = room_ids.copy()
                    room_ids_copy.append(item[0])
                q.enqueue(room_ids_copy)


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
auth = {
    "Authorization": "Token 2330ee34073008c724a7066470b88940e7278f5c"}
# eli_auth
eli_auth = {"Authorization": "Token a39b9cc5b11d49d162694cfee69a4710093b2106"}


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
    data = requests.post(baseUrl + MINE_URL, headers=auth,
                         json=postData).json()
    if data != None:
        print(data)
        return data, 200
    else:
        return ({
            'Error': 'No data returned.'
        })


def dfs(self, starting_room, destination_room, room_ids=None, visited=None,):
    q = Queue()
    if visited == None:
        visited = set()
    if room_ids == None:
        room_ids = [starting_room]
    q.enqueue(room_ids)
    # directions = []

    while q.size() > 0:
        current_room = q.dequeue()

        if current_room == destination_room:
            return room_ids

        if current_room[-1] not in visited:
            visited.add(current_room[-1])

            for key, value in self.rooms[current_room]:
                room_ids_copy = room_ids.copy()
                room_ids_copy.append(key)
# print(tresureSell())
# print(tresurePickup())
# print(carry())
# print(changeName())
# print(checkStatus())
# print(move())
# print(init())


visited = {}


# proof_of_work = -2396423964179274
# last_proof = getLastProof()[0]
# last_proof_num = last_proof['proof']
# last_proof_difficulty = last_proof['difficulty']
# hash_str = hashlib.sha256(
#     f"{last_proof_num}{proof_of_work}".encode()).hexdigest()

# dif = ''
# while hash_str[:last_proof_difficulty] != dif.zfill(last_proof_difficulty):
#     proof_of_work += 1
#     hash_str = hashlib.sha256(
#         f"{last_proof_num}{proof_of_work}".encode()).hexdigest()

# mine(proof_of_work)

# connected_rooms = open('connected_rooms.txt', 'r+')
# for line in connected_rooms:
#     room_info = line.split(':', 1)
#     visited[int(room_info[0])] = ast.literal_eval(room_info[1].strip())
# connected_rooms.close()

# dt = DestinationTraversal()


# starting = init()[0]['room_id']
# print(dt.dfs(visited, starting, 55))


# opposites = {"n": "s", "s": "n", "e": "w", "w": "e"}
# backtrack_directions = []

# # Create a stack and push current data onto the stack
# stack = Stack()
# current_data = init()

# stack.push(current_data)
# # While there are items in the stack...
# while stack.size() > 0:
#     print(f"Visited: {visited}, Backtrack_Directions: {backtrack_directions}")

#     all_exits_explored = True
#     current_data = stack.pop()
#     print('CURRENT DATA', current_data)
#     room_id = current_data[0].get('room_id')
#     room_exits = current_data[0].get('exits')
#     print('exits', room_exits)
#     # If room is not in visited dictionary, add it
#     status = checkStatus()
#     print(status)
#     if room_id not in visited:
#         visited[room_id] = {"n": "?", "s": "?", "e": "?", "w": "?"}
#     # if 'Shrine' in current_data[0]['title']:
#     #     lambdaShrineUWU()

#     # if current_data[0]['items'] and len(current_data[0]['items']) != 0 and status[0]['encumbrance'] < status[0]['strength']:
#     #     for item in current_data[0]['items']:
#     #         treasure_pickup = treasurePickup(item)
#     #         print(treasure_pickup)

#     for d in room_exits:
#         # If direction has not been explored, move that direction and set all_exits_explored = False
#         if visited[room_id][d] != "?":
#             continue
#         else:
#             all_exits_explored = False
#             print("Direction", d)
#             new_data = move(d)
#             # Push opposite direction to backtrack_directions list
#             backtrack_directions.append(opposites[d])
#             # Get new room id and add it to the direction value of the current room in visited
#             new_room_id = new_data[0].get('room_id')

#             print('new_room_id', new_room_id)
#             visited[room_id][d] = new_room_id

#             # # If new room is not in visited, add it
#             if new_room_id not in visited:
#                 visited[new_room_id] = {
#                     "n": "?", "s": "?", "e": "?", "w": "?"}
#                 # Add the last room's id to the current room's values in visited
#             visited[new_room_id][opposites[d]] = room_id
#             print('visited', visited)

#             # Push new room onto the stack
#             stack.push(new_data)
#             break
#     # If all exits have been explored for the current room, backtrack and add room onto the stack
#     if all_exits_explored == True:
#         connected_rooms.write(
#             f"{room_id}: {visited[room_id]}\n")
#         back_direction = backtrack_directions.pop()
#         new_data = move(back_direction)

#         stack.push(new_data)
# connected_rooms.close()

# print(room_id)
# print(room_exits)
# r = requests.get(url=node + "/api/adv/init/", json=get_data)
# print(r.json())
# # data = json.dumps(r)
# # print(data)
