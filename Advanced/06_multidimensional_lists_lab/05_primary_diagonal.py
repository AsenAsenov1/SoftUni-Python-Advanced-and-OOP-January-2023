rows_cols = int(input())

matrix = []
total_sum = 0

"""
1 2 3
4 5 6
7 8 9
"""

for _ in range(rows_cols):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

for row_col in range(rows_cols):
    value = matrix[row_col][row_col]
    total_sum += value

print(total_sum)
