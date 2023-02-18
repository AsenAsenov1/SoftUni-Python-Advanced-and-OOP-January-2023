"""
You will be given N and M – integers, indicating the playground’s dimensions. On the next N lines, you will receive the
rows of the playground, with M columns. You will be marked with the letter 'B', and placed in a random position.
In random positions, furniture or other obstacles will be marked with the letter 'O'. The other players (opponents)
will be marked with the letter 'P'. There will always be three other players participating in the game.
All of the empty positions will be marked with '-'.
Your goal is to touch as many players as possible during the game, without leaving the playground or stepping on an obstacle.
On the next few lines, until you receive the command "Finish", you will receive a few lines with commands representing
which direction you need to move. The possible directions are "up", " down", "right", and "left". If the direction leads
you out of the field, you need to stay in position inside the field(do NOT make the move). If you have an obstacle,
towards the direction, do NOT make the move and wait for the next command.
You need to keep track of the count of touched opponents and the moves you’ve made.
In case you step on a position marked with '-', increase the count of the moves made.
When you receive a command with direction, you check the position you need to step on for an obstacle or opponent.
If there is an opponent, you touch him and the position is marked with '-'(increase the count of the touched opponents
and moves made), and this is your new position.
The game is over when you manage to touch all other opponents or the given command is "Finish". A game report is printed
on the Console:
"Game over!"
"Touched opponents: {count} Moves made: {count}"

INPUT:
4 4
O B O -
- P O P
- - P -
- - - -
left
right
down
right
down
right
up
right
up
down
Finish
"""

row_size, col_size = [int(x) for x in input().split()]
matrix = []
row, col = [0, 0]
OBSTACLE = "O"
OPPONENT = "P"
EMPTY = "-"
PLAYER = "B"
touched_opponents = 0
moves = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row_index in range(row_size):
    current_row = input().split()
    matrix.append(current_row)
    if "B" in current_row:
        row, col = [row_index, current_row.index("B")]

while touched_opponents < 3:
    direction = input()
    if direction == "Finish":
        break

    r, c = directions[direction]

    if row + r < 0 or col + c < 0 or row + r >= row_size or col + c >= col_size:
        continue

    position = matrix[row + r][col + c]

    if position == OBSTACLE:
        continue

    row += r
    col += c

    if position == OPPONENT:
        matrix[row][col] = EMPTY
        touched_opponents += 1
        moves += 1

    elif position == EMPTY:
        moves += 1
        matrix[row - r][col - c] = EMPTY
        matrix[row][col] = PLAYER

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves}")
