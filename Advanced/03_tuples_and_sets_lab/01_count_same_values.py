numbers_input = list(map(float, input().split()))

numbers_count = {number: numbers_input.count(number) for number in numbers_input}

for number, count in numbers_count.items():
    print(f"{number} - {count} times")
