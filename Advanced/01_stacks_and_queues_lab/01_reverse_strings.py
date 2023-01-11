def reverse_stack(stack):
    reversed_stack = []
    stack = list(stack)
    while stack:
        current_char = stack.pop()
        reversed_stack.append(current_char)
    return "".join(reversed_stack)


initial_stack = input()
print(reverse_stack(initial_stack))
