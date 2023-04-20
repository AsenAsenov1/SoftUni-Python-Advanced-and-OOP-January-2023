def fibonacci():
    yield 0
    yield 1

    first_number = 0
    second_number = 1

    while True:
        fibonacci_number = first_number + second_number
        first_number = second_number
        second_number = fibonacci_number
        yield fibonacci_number