rows, cols = [int(x) for x in input().split(", ")]

matrix = []

"""
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
"""

for row in range(rows):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

for column in range(cols):
    columns_sum = 0
    for row in range(rows):
        current_value = matrix[row][column]
        columns_sum += current_value
    print(columns_sum)
