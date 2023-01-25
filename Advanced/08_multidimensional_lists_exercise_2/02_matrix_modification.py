matrix_size = int(input())

matrix = []

for _ in range(matrix_size):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

while True:
    command = input().split()
    if "END" in command:
        break
    action = command[0]
    row, col, value = [int(x) for x in command[1:]]

    if row in range(matrix_size) and col in range(matrix_size):
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

[print(*x) for x in matrix]
