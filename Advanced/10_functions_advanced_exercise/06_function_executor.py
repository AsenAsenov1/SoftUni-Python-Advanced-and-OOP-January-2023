def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []
    for func_ref, func_params in args:
        func_result = func_ref(*func_params)
        result.append(f"{func_ref.__name__} - {func_result}")
    return "\n".join(result)


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))

# Output:
# sum_numbers - 3
# multiply_numbers - 8
