import numpy as np

# Create an empty 3x3 grid
grid = np.zeros((3, 3), dtype=str)

# Initialize players (X and O)
players = ["X", "O"]
current_player = 0  # Start with player X

# Main game loop
while True:
    print(grid)

    # Get the current player's move (row and column)
    row = int(input(f"Player {players[current_player]}, enter row (0-2): "))
    col = int(input(f"Player {players[current_player]}, enter column (0-2): "))

    # Check if the cell is empty
    if grid[row, col] == "":
        grid[row, col] = players[current_player]
    else:
        print("Cell already occupied. Try again.")
        continue

    # Check for a win
    for i in range(3):
        if all(grid[i, j] == players[current_player] for j in range(3)) or \
           all(grid[j, i] == players[current_player] for j in range(3)) or \
           grid[0, 0] == grid[1, 1] == grid[2, 2] == players[current_player] or \
           grid[0, 2] == grid[1, 1] == grid[2, 0] == players[current_player]:
            print(f"Player {players[current_player]} wins!")
            break

    # Switch players
    current_player = 1 - current_player

    # Check for a tie
    if np.all(grid != ""):
        print("It's a tie!")
        break
