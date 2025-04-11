'''
This Python script is creating a 2-dimensional grid of rooms and setting a player's location in the first room.

The first line initialises an empty list named rooms. This list will be used to store the grid of rooms.

The next block of code is a nested loop that fills the rooms list. The outer loop runs 5 times, and each iteration appends an empty list to rooms. This creates a list of lists, effectively creating rows in our 2D grid.

The inner loop also runs 5 times. In each iteration, it appends a string to the current list (or row) in rooms. This string represents a room and is formatted as "Room {i+1}{j+1}", where {i+1} and {j+1} are the current row and column numbers, respectively. This creates the columns in our 2D grid.

After the loops finish executing, rooms is a 5x5 grid where each cell contains a string representing a room.
'''

rooms = []

for i in range(5):
    rooms.append([])
    for j in range(5):
        rooms[i].append(f"Room {i+1}{j+1}")
    
print(rooms)

set_player_location = rooms[0][0]

print(f"the player location is: {set_player_location}")