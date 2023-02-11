def fib_create(number):
    fib_list = [0, 1]

    for i in range(2, number):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list


def fib_locate(number, fibo_list):
    if number in fibo_list:
        return f"The number - {number} is at index {fibo_list.index(number)}"
    else:
        return f"The number {number} is not in the sequence"
