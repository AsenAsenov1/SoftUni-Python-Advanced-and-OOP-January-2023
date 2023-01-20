rows = int(input())

even_matrix = []

for _ in range(rows):
    current_row = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    even_matrix.append(current_row)

print(even_matrix)
