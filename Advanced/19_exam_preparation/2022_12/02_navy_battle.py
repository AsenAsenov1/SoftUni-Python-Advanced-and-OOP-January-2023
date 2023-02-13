size = int(input())
matrix = []
row, col = [0, 0]
damage = 0
cruisers_destroyed = 0
MINE, CRUISER, SUBMARINE = "*", "C", "S"

for r in range(size):
    current_row = list(input())
    if "S" in current_row:
        row = r
        col = current_row.index("S")
    matrix.append(current_row)

directions = {"up": [-1, 0],
              "down": [1, 0],
              "left": [0, -1],
              "right": [0, 1]
              }

while True:
    command = input()
    r, c = directions[command]
    matrix[row][col] = '-'
    row, col = row + r, col + c

    if matrix[row][col] == CRUISER:
        cruisers_destroyed += 1
        if cruisers_destroyed == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            matrix[row][col] = SUBMARINE
            break
    elif matrix[row][col] == MINE:
        damage += 1
        if damage == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            matrix[row][col] = SUBMARINE
            break

[print("".join(x)) for x in matrix]
