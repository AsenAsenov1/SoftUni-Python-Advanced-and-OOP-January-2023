def match_parent(eq: str):
    stack = list(eq)
    indexes = []
    for index in range(len(stack)):
        if stack[index] == '(':
            indexes.append(index)
        elif stack[index] == ')':
            opening_bracket = int(indexes.pop())
            print("".join((stack[opening_bracket:index + 1])))


equation = input()
match_parent(equation)
