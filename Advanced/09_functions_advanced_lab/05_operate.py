def operate(operator, *args):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        return args[0] - sum(args[1:])
    elif operator == "*":
        result = 1
        for num in args:
            result *= num
        return result
    elif operator == "/":
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
    else:
        return "Invalid operator"


print(operate("-", 5, 4, 3))
