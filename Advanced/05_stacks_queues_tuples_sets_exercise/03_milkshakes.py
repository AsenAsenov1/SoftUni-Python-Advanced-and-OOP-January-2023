from collections import deque

chocolate = [int(x) for x in input().split(", ")]
milk = deque([int(x) for x in input().split(", ")])
prepared_milkshakes = 0

while chocolate and milk and prepared_milkshakes < 5:
    current_chocolate = chocolate.pop()
    current_milk = milk.popleft()

    if current_chocolate and current_milk <= 0:
        continue
    if current_chocolate <= 0:
        milk.appendleft(current_milk)
        continue
    if current_milk <= 0:
        chocolate.append(current_chocolate)
        continue

    if current_chocolate == current_milk:
        prepared_milkshakes += 1
    else:
        milk.append(current_milk)
        chocolate.append(current_chocolate - 5)

if prepared_milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join([str(x) for x in milk])}")
else:
    print("Milk: empty")
