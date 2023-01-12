from collections import deque

queue = deque()
init_water_quantity = int(input())

while True:
    name = input()
    if name == "Start":
        break
    queue.append(name)

while True:
    quantity = input()
    if quantity == "End":
        break
    elif quantity.startswith("refill"):
        refill_quantity = quantity.split()[1]
        init_water_quantity += int(refill_quantity)
    else:
        if int(quantity) <= init_water_quantity:
            print(f"{queue[0]} got water")
            queue.popleft()
            init_water_quantity -= int(quantity)
        else:
            print(f"{queue[0]} must wait")
            queue.popleft()

print(f"{init_water_quantity} liters left")
