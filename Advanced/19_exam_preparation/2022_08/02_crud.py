"""
In the beginning, you will be given a matrix with 6 rows and 6 columns representing a table with information.
It consists of:
•	Letters - on one or many positions in the table
•	Numbers - on one or many positions in the table
•	Empty positions - marked with "."

Next, you will receive your first position on the table in the format "({row}, {column})"
On the following lines, until you receive "Stop" you will be receiving commands in the format:
•	"Create, {direction}, {value}"
o	The direction could be "up", "down", "left" or "right"
o	If you step in an empty position, create the given value on that position. E.g., if the given value is "A", and the position is empty (".") - change it to "A"
o	If the position is NOT empty, do NOT create a value on that position
•	"Update, {direction}, {value}"
o	The direction could be "up", "down", "left" or "right"
o	If you step on a letter or number, update the position with the given value. E.g., if the given value is "h", and the position's value is "12" - change it to "h"
o	If the position is empty, do NOT update the value on that position
•	"Delete, {direction}"
o	The direction could be "up", "down", "left" or "right"
o	If you step on a letter or number, delete it, and empty the position. E.g., if the given position's value is "h" - change it to "."
o	If the position is already empty, do NOT delete it
•	"Read, {direction}"
o	The direction could be "up", "down", "left" or "right"
o	If you step on a letter or number, print it on the console
o	If the position is empty, do NOT read it
You can make only ONE move at a time in the given direction for each command given.
In the end, print the final matrix.

INPUT:
H 8 . . . .
70 i . . . .
t . . . B .
50 . 16 . C .
. . . t . .
. 25 . . . .
(0, 0)
Read, right
Read, down
Read, left
Delete, down
Create, right, 10
Read, left
Stop

OUTPUT:
8
i
70
H 8 . . . .
70 i . . . .
. 10 . . B .
50 . 16 . C .
. . . t . .
. 25 . . . .
"""

SIZE = 6
EMPTY = "."
matrix = []

for row in range(SIZE):
    matrix.append(input().split())

row, col = (int(x) for x in input().replace("(", "").replace(")", "").split(", "))
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command_line = input()
    if command_line == "Stop":
        break

    command_split = command_line.split(", ")
    action = command_split[0]
    direction = command_split[1]
    r_increase, c_increase = directions[direction]
    row += r_increase
    col += c_increase
    current_position = matrix[row][col]

    if action == "Create":
        value = command_split[2]
        if current_position == EMPTY:
            matrix[row][col] = value

    elif action == "Read":
        if current_position.isalnum():
            print(matrix[row][col])

    elif action == "Update":
        value = command_split[2]
        if current_position.isalnum():
            matrix[row][col] = value

    elif action == "Delete":
        if current_position.isalnum():
            matrix[row][col] = EMPTY

[print(*x) for x in matrix]
