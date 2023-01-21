matrix_size = int(input())

primary_values = []
secondary_values = []

for index in range(matrix_size):
    current_row = [int(x) for x in input().split(", ")]
    primary = current_row[index]
    secondary = current_row[matrix_size - index - 1]
    primary_values.append(primary)
    secondary_values.append(secondary)

print(f"Primary diagonal: {', '.join(map(str, primary_values))}. Sum: {sum(primary_values)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_values))}. Sum: {sum(secondary_values)}")
