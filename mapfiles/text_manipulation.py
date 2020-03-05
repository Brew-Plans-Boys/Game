import json
import ast

#Load Data


raw = open("rooms_x554.txt", "r")
roomList = raw.readlines()


all_rooms = []

#with open('clean_rooms.txt', 'w') as cleaned:
for room in roomList:
    all_rooms.append(ast.literal_eval(room))
    #cleaned.write(room)
#print(f"ALL ROOMS: {all_rooms}")
# lowest_val = all_rooms[0]['room_id']
# print("Lowest_Val: ", lowest_val)
#print(all_rooms[0:5])
cleaned_rooms = []
for room in all_rooms:
    # print(f"room: {room}", "\n")
    room_id = room['room_id']
    coordinates = room['coordinates']
    exits = room['exits']
    # print(f"ROOM: {room}, Room_id: {room_id}")

    clean = {"room_id":room_id, "coordinates":coordinates, "exits":exits}

    if clean not in cleaned_rooms:
        cleaned_rooms.append(clean)


    # print(f"clean: {clean}")

print(cleaned_rooms)
print(len(cleaned_rooms))


with open('clean_rooms.txt', 'w') as cleaned:
    cleaned.write(json.dumps(cleaned_rooms, indent = 4))

# for room in all_rooms:
#     print(room.keys)
    
# with open('clean_rooms.txt', 'w') as cleaned:

# for line in raw.split("n"):
#     print(line)
#     print(line["room_id"])
# raw_data = open('rooms_x554.txt', 'r+')
# print(raw_data)

# read_data = raw_data.read()
# print(read_data, "==============")
# rooms = {}
# z = raw_data.read()
# for line in z:
#     rooms[]
# print(rooms)
# raw_data.close()

# for room in raw_data:
#     # room = ast.literal_eval(room)
#     print(f"Room: {room}", '\n')
#     rooms.add(room)
# print(rooms, "\n")
#     # f.write(json.dumps(room, indent = 4))


# with open('clean_rooms.txt', 'w') as f:
#     f.write(json.dumps(rooms, indent=4))

# # raw = open(raw_data, 'rt')
# # text = raw.read()
# # raw.close()

# # for room in text:
# #     print(f"{room} ")


# # raw_data = # with open('mapfiles/rooms.txt', 'w') as f:
# #     #     f.write(json(data) + '\n')

# # raw = with open('rooms.txt', 'r') as f:
# # f.write()


