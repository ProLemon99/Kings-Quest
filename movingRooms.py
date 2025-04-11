'''
This Python script is creating a simple text-based game environment using a dictionary to represent rooms. Each room is a dictionary itself, containing details about the room such as its name, description, exits (other rooms it connects to), and enemies present in the room.

The rooms dictionary is structured with integer keys representing room numbers, and the values are nested dictionaries holding the room details. For example, rooms[1] would give you the dictionary {"name": "Room 1", "description": "This is room 1", "exits": ["Room 2"], "enemies": "Goblin"}.

The player's location is set by assigning one of the room dictionaries to the player_location variable. In this case, player_location = rooms[3] sets the player's location to Room 3.

The script then prints various details about the player's current location. The player_location variable is used to access the details of the room the player is currently in. For example, player_location['name'] would give you the name of the current room, and player_location['enemies'] would give you the enemy present in the current room.

The print statements are used to display the current room's details to the player. The first print statement is a debug statement that prints the entire room dictionary. The following print statements inform the player of the room they are in, the description of the room, the enemy in the room, and the exits from the room.


'''

# create a dictionary to holdroom s. Each room will have a name, description, exits and enemies
rooms = {
    1: {"name": "Room 1", "description": "This is room 1", "exits": ["Room 2"], "enemies": "Goblin"},
    2: {"name": "Room 2", "description": "This is room 2", "exits": ["Room 1"], "enemies": "Orc"},
    3: {"name": "Room 3", "description": "This is room 3", "exits": ["Room 2", "Room 1"], "enemies": "Rick Astley"}
}

# set player location to a room in the dictionary
player_location = rooms[3]

print(f" DEBUG: the room the player is in: {player_location}")

print(f"You are in: {player_location['name']}")

print(f"{player_location['description']}")

print(f"There is a dangerous {player_location['enemies']} here")

print(f"You can go to: {player_location['exits']}")