number_of_names = int(input())

unique_names = set([input() for name in range(number_of_names)])

print("\n".join(unique_names))
