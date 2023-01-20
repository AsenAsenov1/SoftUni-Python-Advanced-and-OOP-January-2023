rows = int(input())

matrix = []

for _ in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    matrix.extend(current_row)

print(matrix)
