def is_valid(rows_size, cols_size, row1, col1, row2, col2):
    if 0 <= row1 < rows_size and 0 <= row2 < rows_size:
        if 0 <= col1 < cols_size and 0 <= col2 < cols_size:
            return True
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    current_row = input().split()
    matrix.append(current_row)

while True:
    command = input().split()
    if command[0] == "END":
        break

    if command[0] == "swap" and len(command) == 5:
        row1, col1, row2, col2 = [int(x) for x in command[1:]]
        if is_valid(rows, cols, row1, col1, row2, col2):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

            for matrix_row in matrix:
                print(*matrix_row)
    else:
        print("Invalid input!")
