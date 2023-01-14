number = int(input())
stack = []
reversed_stack = []

for _ in range(number):
    command_input = input().split()
    command = command_input[0]

    if command == '1':
        number = command_input[1]
        stack.append(int(number))
    elif command == '2' and stack:
        stack.pop()
    elif command == '3' and stack:
        print(max(stack))
    elif command == '4' and stack:
        print(min(stack))

while stack:
    popped_number = stack.pop()
    reversed_stack.append(str(popped_number))

print(", ".join(reversed_stack))
