def even_numbers(function):

    def wrapper(numbers):
        return [number for number in numbers if number % 2 == 0]

    return wrapper