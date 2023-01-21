rows, cols = [int(x) for x in input().split()]

# matrix = []

for row in range(rows):
    current_row = []
    for col in range(cols):
        substring = f"{chr(97 + row)}{chr(97 + (row + col))}{chr(97 + row)}"
        current_row.append(substring)
    # matrix.append(current_row)
    print(*current_row)

# print(matrix)
