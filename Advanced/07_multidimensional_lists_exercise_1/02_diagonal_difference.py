matrix_size = int(input())

primary_values = []
secondary_values = []

for index in range(matrix_size):
    current_row = [int(x) for x in input().split()]
    primary = current_row[index]
    secondary = current_row[matrix_size - index - 1]
    primary_values.append(primary)
    secondary_values.append(secondary)

difference = abs(sum(primary_values) - sum(secondary_values))

print(difference)
