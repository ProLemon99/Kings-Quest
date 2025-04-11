# Initialize the grid
grid = [['X', 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

# Player position
player_row = 0
player_col = 0

# Function to display the grid
def display_grid():
    for row in grid:
        print(" ".join(map(str, row)))

# Function to check if all rooms are visited
def all_visited():
    for row in grid:
        for cell in row:
            if cell == 0:
                return False
    return True

# Main game loop
while not all_visited():
    # Display the grid
    print("Current Grid:")
    display_grid()
    
    # Get user input for movement
    direction = input("Enter N/S/E/W to move: ").upper()
    
    # Update player position based on user input
    if direction == "N":
        # Move up
        if player_row > 0:
            grid[player_row][player_col] = 1
            player_row -= 1
        else:
            print("You can't go that way!")
    elif direction == "S":
        # Move down
        if player_row < 2:
            grid[player_row][player_col] = 1
            player_row += 1
        else:
            print("You can't go that way!")
    elif direction == "E":
        # Move right
        if player_col < 2:
            grid[player_row][player_col] = 1
            player_col += 1
        else:
            print("You can't go that way!")
    elif direction == "W":
        # Move left
        if player_col > 0:
            grid[player_row][player_col] = 1
            player_col -= 1
        else:
            print("You can't go that way!")
    else:
        print("Invalid input! Please enter N/S/E/W.")
    
    # Update player position on the grid
    grid[player_row][player_col] = 'X'

# All rooms visited
print("Congratulations! You have visited all rooms.")
