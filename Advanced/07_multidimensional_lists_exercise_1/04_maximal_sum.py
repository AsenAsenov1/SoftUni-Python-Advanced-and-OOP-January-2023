import sys

rows, cols = [int(x) for x in input().split()]

matrix = []
highest_score = -sys.maxsize
best_matrix = []

for _ in range(rows):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

for row in range(rows - 2):
    for col in range(cols - 2):
        num1, num2, num3 = matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]
        num4, num5, num6 = matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]
        num7, num8, num9 = matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]
        total_sum = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9

        if total_sum > highest_score:
            best_matrix.clear()
            highest_score = total_sum
            best_matrix = [
                [num1, num2, num3],
                [num4, num5, num6],
                [num7, num8, num9]
            ]
print("Sum =", highest_score)

for row in best_matrix:
    [print(int(x), end=" ") for x in row]
    print()

