import json
import time
import random

from usingExternalFileForTextWithPauses import readPhrases # reads attack phrases
from usingExternalFileForTextWithPauses import clearScreen

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
            "name": "Room 1",  # Name of the room
            "description": "This is room 1",  # Description of the room
            "exits": ["Room 2"],  # List of rooms that can be accessed from this room
            "enemies": "Goblin"
        },
        {
            "name": "Room 2",  # Name of the room
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

clearScreen()

print(f"DEDUG: Rooms: {rooms} Enemies: {enemies}")

# create a list of actions the player can input
actions = ["move", "attack", "defend", "help", "quit"]

# set the player location to the first room
player_location = 1

def readTextFileWithPauses():
    # open the file called someRandomStoryText.txt. Change this file name
    with open("someRandomStoryText.txt") as file:
        # load the file into a variable
        text = file.read()
    # split the text into sentences
    sentences = text.split(".")
    # loop through the sentences
    for sentence in sentences:
        # print the sentence
        print(sentence)
        # pause for 1 second
        time.sleep(.25)

# print the player location
print(f"You are currently in {rooms[player_location-1]['description']}")