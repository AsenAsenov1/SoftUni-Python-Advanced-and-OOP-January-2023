from collections import deque

chocolates = [int(i) for i in input().split(", ")]
milk_cups = deque(int(i) for i in input().split(", "))

milkshakes = 0

while milkshakes < 5 and chocolates and milk_cups:
    chocolate = chocolates.pop()
    milk = milk_cups.popleft()

    if chocolate <= 0 and milk <= 0:
        continue
    elif chocolate <= 0:
        milk_cups.appendleft(milk)
        continue
    elif milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        milk_cups.append(milk)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join(map(str, milk_cups))}")
else:
    print("Milk: empty")