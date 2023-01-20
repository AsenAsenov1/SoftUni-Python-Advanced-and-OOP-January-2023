rows, cols = [int(x) for x in input().split(", ")]

matrix = []
total_sum = 0

for rows in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    total_sum += sum(current_row)
    matrix.append(current_row)

print(total_sum)
print(matrix)
