number = int(input())

elements_set = set()

for _ in range(number):
    elements_input = input().split()
    for element in elements_input:
        elements_set.add(element)

print("\n".join(elements_set))
