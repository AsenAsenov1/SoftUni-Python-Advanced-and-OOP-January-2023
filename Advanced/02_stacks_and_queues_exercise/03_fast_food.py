from collections import deque

food_quantity = int(input())
orders = list(map(int, input().split()))
orders_deque = deque(orders)
completed = True

print(max(orders))

while food_quantity >= 0 and orders_deque:
    current_order_value = orders_deque[0]

    if food_quantity - current_order_value >= 0:
        orders_deque.popleft()
        food_quantity -= current_order_value
    else:
        completed = False
        break

if completed:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(list(map(str, orders_deque)))}")
