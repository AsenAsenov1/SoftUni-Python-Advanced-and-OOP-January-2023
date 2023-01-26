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
 


print(operate("+",1,2,3,4)) # Output: 10
print(operate("-",1,2,3,4)) # Output: -8
print(operate("*",1,2,3,4)) # Output: 24
print(operate("/",1,2,3,4)) # Output: 0.041666666666666664
