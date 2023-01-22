from collections import deque

rows, cols = [int(x) for x in input().split()]
text = input()
snake = deque(text)
matrix = []

for row in range(rows):
    current_row = []

    for col in range(cols):
        char = snake.popleft()
        snake.append(char)
        current_row.append(char)

    if row % 2 == 0:
        matrix.append(current_row)
    else:
        matrix.append(current_row[::-1])

[print("".join(x)) for x in matrix]
