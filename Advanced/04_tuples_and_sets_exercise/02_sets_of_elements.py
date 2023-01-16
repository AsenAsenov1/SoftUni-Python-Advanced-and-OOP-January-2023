num1, num2 = list(map(int, input().split()))

set1 = set()
set2 = set()

for counter in range(1, (int(num1) + int(num2)) + 1):
    current_number = input()
    if counter <= num1:
        set1.add(current_number)
    else:
        set2.add(current_number)

result = set1.intersection(set2)

print("\n".join(result))
