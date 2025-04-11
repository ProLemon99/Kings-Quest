# What is this file about

# In this code, a dictionary named enemies is defined. It contains information about different types of enemies that can be encountered in a game.

# The keys in the enemies dictionary are the names of the enemies, such as "Goblin", "Orc", and "Troll".
# The values associated with each enemy name are sub-dictionaries that contain information about the enemy's attributes, including health, attack, and defense.

# For example, the "Goblin" enemy has a health of 10, an attack of 2, and a defense of 1.

# The code is useful for storing and accessing information about different types of enemies in a game. It allows easy retrieval of enemy attributes based on their names.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

# Print the list of rooms and their information
for room in rooms:  # Loop through each room
    print("Room:", room['name'])  # Print the name of the room
    print("Description:", room['description'])  # Print the description of the room
    print("Exits:", room['exits'])  # Print the list of rooms that can be accessed from this room
    print()  # Print a blank line to separate the rooms

# Print the enemy information
for enemy_name, enemy_stats in enemies.items():
    print("Name of enemy:", enemy_name)
    print("Health of enemy:", enemy_stats["health"])
    print("Attack of enemy:", enemy_stats["attack"])
    print("Defense of enemy:", enemy_stats["defense"])
    print()