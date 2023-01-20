"""
ABC
DEF
X!@
"""

rows = int(input())
matrix = [[x for x in input()] for y in range(rows)]
symbol = input()
symbol_found = False

for row in range(rows):
    for col in range(rows):
        current_symbol = matrix[row][col]
        if current_symbol == symbol:
            print(f"({row}, {col})")
            symbol_found = True
            break
    if symbol_found:
        break
else:
    print(f"{symbol} does not occur in the matrix")
