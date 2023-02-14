"""
On the first line, you will receive a sequence of numbers representing milligrams of caffeinе.
On the second line, you will receive another sequence of numbers representing energy drinks. It is important to know that
the maximum caffeine Stamat can have for the night is 300 milligrams, and his initial is always 0.
To calculate the caffeine in the drink take the last milligrams of caffeinе and the first energy drink, and multiply them.
Then, compare the result with the caffeine Stamat drank:
•	If the sum of the caffeine in the drink and the caffeine that Stamat drank doesn't exceed 300 milligrams, remove both t
he milligrams of caffeinе and the drink from their sequences. Also, add the caffeine to Stamat's total caffeine.
•	If Stamat is about to exceed his maximum caffeine per night, do not add the caffeine to Stamat’s total caffeine.
Remove the milligrams of caffeinе and move the drink to the end of the sequence. Also, reduce the current caffeine that
Stamat has taken by 30 (Note: Stamat's caffeine cannot go below 0).
Stop calculating when you are out of drinks or milligrams of caffeine.

Input:
34, 2, 3
40, 100, 250

Output:
Drinks left: 100, 250
Stamat is going to sleep with 60 mg caffeine.
"""

from collections import deque

caffeine_stack = [int(x) for x in input().split(", ")]
energy_drinks_que = deque(int(x) for x in input().split(", "))
MAX_QUANTITY = 300
current_caffeine = 0

while caffeine_stack and energy_drinks_que:
    caffeine = caffeine_stack.pop()
    drink = energy_drinks_que.popleft()
    result = caffeine * drink

    if current_caffeine + result <= MAX_QUANTITY:
        current_caffeine += result
    else:
        energy_drinks_que.append(drink)

        if current_caffeine - 30 < 0:
            current_caffeine = 0
        else:
            current_caffeine -= 30

if energy_drinks_que:
    print(f"Drinks left: {', '.join(map(str, energy_drinks_que))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")
