#    This is a modified verions of Getting User input

#    Here, a function is created to manage the user input.

#    The first code block is responsible for displaying the possible actions that a player can take in the game.
#    The actions list contains the available actions that the player can choose from.
#    The for loop iterates over each action in the actions list and prints it out.

#    print("You can do the following actions: ")
#    for action in actions:
#        print(action)

#    This code block is used to get the user's input in the game.
#    It calls the get_user_input() function to retrieve the user's input and assigns it to the user_input variable.

#    The user's input is then printed as a debug message for testing purposes.
#
#    get the user input
#    user_input = get_user_input()
#    print(f"DEBUG: This is the action returned from the function {user_input}")

#    This means we can now call a fuction for the whole user_input routine and not have to keep re-making it. 
#    All that happens is the fuction returns the input to the mainline of the program using RETURN and then the variable. 
#    Ie, the function RETURNS the answer or it could be a decision or calculation if we wanted. RETURNing values after a function has been run is a common method.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# create a function to scroll the screen up
def clear_screen():
    print("\n" * 20)

# create a function to get user input
def get_user_input():
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
            return user_input

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

# get the user input
user_input = get_user_input()
print(f"DEBUG: This is the action returned from the function {user_input}")