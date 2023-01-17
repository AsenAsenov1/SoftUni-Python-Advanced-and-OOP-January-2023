from collections import deque

input_line = input().split()
que = deque()

operators = {
    "-": lambda a, b: a - b,
    "+": lambda a, b: a + b,
    "/": lambda a, b: a // b,
    "*": lambda a, b: a * b,
}

for character in input_line:
    if character not in operators:
        que.append(character)
    else:
        result = 0
        while len(que) > 1:
            x = int(que.popleft())
            y = int(que.popleft())
            result = operators[character](x, y)
            que.appendleft(result)
print(*que)
