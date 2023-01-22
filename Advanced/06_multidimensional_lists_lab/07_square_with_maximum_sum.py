import sys

rows, cols = [int(x) for x in input().split(", ")]

matrix = []
highest_score = -sys.maxsize
sub_matrix = []

for row in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    matrix.append(current_row)

for row in range(rows - 1):
    for col in range(cols - 1):
        num1, num2, = matrix[row][col], matrix[row][col + 1]
        num3, num4 = matrix[row + 1][col], matrix[row + 1][col + 1]
        sub_matrix_sum = num1 + num2 + num3 + num4

        if sub_matrix_sum > highest_score:
            highest_score = sub_matrix_sum
            sub_matrix = [[num1, num2],
                          [num3, num4]]

for row in sub_matrix:
    print(*row)

print(highest_score)
