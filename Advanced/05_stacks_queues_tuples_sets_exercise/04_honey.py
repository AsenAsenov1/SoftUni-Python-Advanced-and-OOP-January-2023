from collections import deque

bees_que = deque(map(int, input().split()))
nectar_stack = list(map(int, input().split()))
symbols = deque(input().split())

collected_honey = 0
operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

while nectar_stack and bees_que:
    bee_peek = bees_que[0]
    nectar_peek = nectar_stack[-1]

    if nectar_peek >= bee_peek:
        operator = symbols.popleft()
        a = bees_que.popleft()
        b = nectar_stack.pop()
        if b == 0:
            continue
        result = operators[operator](a, b)
        collected_honey += abs(result)
    else:
        nectar_stack.pop()

print(f"Total honey made: {collected_honey}")

if bees_que:
    print(f"Bees left: {', '.join(map(str, bees_que))}")

if nectar_stack:
    print(f"Nectar left: {', '.join(map(str, nectar_stack))}")
