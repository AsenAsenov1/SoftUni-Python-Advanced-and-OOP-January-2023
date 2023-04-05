def number_increment(numbers):
    def increase():
        increased_numbers = [number + 1 for number in numbers]
        return increased_numbers

    return increase()
