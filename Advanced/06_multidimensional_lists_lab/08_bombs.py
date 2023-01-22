size = int(input())

matrix = [[int(x) for x in input().split()] for x in range(size)]
bombs = [x for x in input().split()]
alive_cells = []
mini_matrix = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1], [0, 0], [0, 1],
    [1, -1], [1, 0], [1, 1]
]

#  For number of bombs
for bomb_count in bombs:
    bomb_row, bomb_col = [int(x) for x in bomb_count.split(",")]
    bomb_value = matrix[bomb_row][bomb_col]

    #  Reduce the values in the range of the explosion
    for number in mini_matrix:
        index_row, index_col = number
        row, col = bomb_row + index_row, bomb_col + index_col
        if 0 <= row < size > col >= 0:
            if matrix[row][col] > 0:
                matrix[row][col] -= bomb_value

#  Find all alive cells
for matrix_row in matrix:
    [alive_cells.append(x) for x in matrix_row if x > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*x) for x in matrix]

