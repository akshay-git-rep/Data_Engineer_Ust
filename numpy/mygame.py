import numpy as np

grid = np.zeros((3,3),dtype="str")

players = ["x","o"]
current_player = 0

while True:
    print(grid)

    row = int(input(f"Player {players[current_player]} enter the row index:"))
    col = int(input(f"Player {players[current_player]} enter the column index:"))

    if grid[row,col] == "":
        grid[row,col] = players[current_player]
    else:
        print("cell is already occipied")

    for i in range(3):
        #print("I value is :", i)
        if all(grid[i,j] == players[current_player] for j in range(3)) or \
           all(grid[j,i] == players[current_player] for j in range(3)) or \
           grid[0,0] == grid[1,1] == grid[2,2] == players[current_player] or \
           grid[0,2] == grid[1,1] == grid[2,0] == players[current_player]:
            #print("if I value is :", i,"if J value is :", j)
            print(f"Player {players[current_player]} wins!")
            break

    current_player = 1 - current_player

    if np.all(grid != ""):
        print("its a tie match!")
        break
