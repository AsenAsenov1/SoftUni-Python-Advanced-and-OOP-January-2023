rows, cols = [int(x) for x in input().split()]

matrix = []
found_chars = 0

#  Create matrix
for _ in range(rows):
    current_row = input().split()
    matrix.append(current_row)

#  Iterate through the matrix
for row in range(rows - 1):
    for col in range(cols - 1):
        num1 = matrix[row][col]
        num2 = matrix[row][col + 1]
        num3 = matrix[row + 1][col]
        num4 = matrix[row + 1][col + 1]
        if num1 == num2 == num3 == num4:
            found_chars += 1

print(found_chars)
