def get_primes(numbers: list):
    for number in numbers:
        if number > 1:
            for num in range(2, number):
                if number % num == 0:
                    break
            else:
                yield number