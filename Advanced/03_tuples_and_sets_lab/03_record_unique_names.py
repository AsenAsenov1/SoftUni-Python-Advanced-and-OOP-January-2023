number = int(input())

set_of_names = set()

for _ in range(number):
    set_of_names.add(input())

print('\n'.join(set_of_names))
