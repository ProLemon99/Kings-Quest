#   The first block of code contains a dictionary named enemies, which stores information about different types of enemies in the game.
#   Each enemy is a key-value pair in the dictionary, where the key represents the enemy's name (e.g., "Goblin", "Orc", "Troll"), and the value is another dictionary containing attributes of the enemy, such as their health, attack, and defense.

#   The next block of code declares a dictionary named game_map that represents the game map.
#   The game_map dictionary contains a key called "rooms", and its corresponding value is a list containing information about different rooms in the game.
#   Each room is represented by a dictionary with keys such as "name", "description", "exits", and "enemies".
#   The "name" key stores the room's name (e.g., "1", "2").
#   The "description" key holds the description of the room.
#   The "exits" key contains a list of other rooms that can be accessed from the current room.
#   The "enemies" key specifies the enemy present in that room.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# create a function to scroll the screen up
def clear_screen():
    print("\n" * 20)    

# Description: This file contains the code for the game map and enemy information.
# this is a dictonary for the enemies in the game
enemies = {
    "Goblin": {"health": 10, "attack": 2, "defense": 1},
    "Orc": {"health": 15, "attack": 3, "defense": 2},
    "Troll": {"health": 20, "attack": 4, "defense": 3}
}

# The code defines a dictionary named 'map' which contains information about rooms.
game_map = {
    "rooms": [
        {
            "name": "1",  # Name of the room
            "description": "This is room 1",  # Description of the room
            "exits": ["Room 2"],  # List of rooms that can be accessed from this room
            "enemies": "Goblin"
        },
        {
            "name": "2",  # Name of the room
            "description": "This is room 2",  # Description of the room
            "exits": ["Room 1"],  # List of rooms that can be accessed from this room
            "enemies": "Orc"
        }
    ]
}

# Get the list of rooms
rooms = game_map['rooms']

# Get the list of enemies
enemies = game_map.get('enemies')

clear_screen()

print(f"DEDUG: Rooms: {rooms} Enemies: {enemies}")

# create a list of actions the player can input
actions = ["move", "attack", "defend", "help", "quit"]

# convert the str in the room list to int as you want to use this to check the player location
for room in rooms:
    room["name"] = int(room["name"])

# set the player location to the first room
player_location = 1

# print the player location
print(f"You are currently in {rooms[player_location-1]['description']}")

#show the player these moves. Action is a list of possible moves
print("You can do the following actions: ")
for action in actions:
    print(action)

# set the current user input state to false
user_input = False

# while the user input is not in the list of actions, keep asking for input
while not user_input:
    user_input = input("What would you like to do? ").lower()
    # if the user input is just the first letter of the action, set the user input to the full action
    if user_input == "m":
        user_input = "move"
    elif user_input == "a":
        user_input = "attack"
    elif user_input == "d":
        user_input = "defend"
    elif user_input == "h":
        user_input = "help"
    elif user_input == "q":
        user_input = "quit"

    # if the user input is not in the list of actions, print an error message and set the user input to false
    if user_input not in actions:
        print(f"Sorry, I can't {user_input} here, try something else")
        user_input = False
    else:
        print(f"You chose: {user_input}")
        break