import random

# Define the rooms
rooms = {
    1: {"name": "Entrance Hall", "description": "You stand in a dimly lit entrance hall. Cobwebs hang from the ceiling."},
    2: {"name": "Torture Chamber", "description": "You enter a chamber filled with rusty instruments of torture."},
    3: {"name": "Treasure Room", "description": "You find yourself in a room glittering with gold and jewels!"},
    4: {"name": "Monster's Lair", "description": "You cautiously step into a dark room filled with growls and roars.", "enemy": "Goblin"}
}

# Define possible exits from each room
exits = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3]
}

# Player starts in the Entrance Hall
current_room = 1

# Function to display current room information
def display_room(room_number):
    print("You are in the", rooms[room_number]["name"])
    print(rooms[room_number]["description"])
    if "enemy" in rooms[room_number]:
        print("Watch out! There's a", rooms[room_number]["enemy"], "here!")

# Main game loop
while True:
    display_room(current_room)

    # Check if there's an enemy in the room
    if "enemy" in rooms[current_room]:
        print("You're under attack by a", rooms[current_room]["enemy"] + "!")
        print("Game Over!")
        break

    # Prompt the player for input
    direction = input("Choose a direction to move (N/S/E/W): ").upper()

    # Check if the direction is valid
    if direction in ["N", "S", "E", "W"]:
        possible_exits = exits[current_room]
        if direction == "N" and current_room in possible_exits:
            current_room = possible_exits[possible_exits.index(current_room) - 1]
        elif direction == "S" and current_room in possible_exits:
            current_room = possible_exits[possible_exits.index(current_room) + 1]
        elif direction == "E" and current_room + 1 in possible_exits:
            current_room += 1
        elif direction == "W" and current_room - 1 in possible_exits:
            current_room -= 1
        else:
            print("You can't go that way!")
    else:
        print("Invalid direction! Please choose N/S/E/W.")