"""
You will be given a sequence of 6 seats - every seat is a mix of a number and a letter in the format "{number}{letter}".
You will also be given two more sequences of numbers only.
First, you have to take the first number of the first sequence and the last number of the second sequence.
Next, take the sum of those two numbers and find its ASCII character.
•	Compare each of the two taken numbers and the found character with the seats. If you find a match,
the passenger is seated, and the seat is considered taken. Remove both numbers from their sequences.
•	If there is no equality, the two numbers should be returned at the end of their sequences (first becomes last, last becomes first).
•	If you match an already taken seat, you should just remove both numbers from their sequences.
Each time you take numbers from the sequences and try to match them, you make one rotation. You should keep track of all rotations made.
The program should end under the following circumstances:
•	You have found 3 (three) seat matches
•	You have made a total of 10 rotations

INPUT:
15C, 25C, 36C, 43P, 40E, 38G
15, 25, 80, 40, 15, 99, 52
15, 42, 29

OUTPUT:
Seat matches: 25C, 40E, 15C
Rotations count: 7
"""

from collections import deque

seats_sequence = input().split(", ")
first_line = deque([int(x) for x in input().split(", ")])
second_line = deque([int(x) for x in input().split(", ")])
rotations = 0
taken_seats = []

while len(taken_seats) < 3 and rotations < 10:
    first_number = first_line.popleft()
    second_number = second_line.pop()
    character = chr(first_number + second_number)
    seats = (str(first_number) + character, str(second_number) + character)

    for current_seat in seats:
        if current_seat in seats_sequence:
            if current_seat not in taken_seats:
                taken_seats.append(current_seat)
                break

    else:
        first_line.append(first_number)
        second_line.appendleft(second_number)

    rotations += 1

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")
