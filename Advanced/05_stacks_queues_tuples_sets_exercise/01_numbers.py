set1 = set(int(x) for x in input().split())
set2 = set(int(x) for x in input().split())
number_of_commands = int(input())

for _ in range(number_of_commands):
    input_command = input().split()
    action = " ".join(input_command[:2])
    numbers = set(int(x) for x in input_command[2:])

    if action == "Add First":
        set1 = set1.union(numbers)
    elif action == "Add Second":
        set2 = set2.union(numbers)
    elif action == "Remove First":
        set1 = set1.difference(numbers)
    elif action == "Remove Second":
        set2 = set2.difference(numbers)
    elif action == "Check Subset":
        print(set1.issubset(set2) or set2.issubset(set1))

print(*sorted(set1), sep=", ")
print(*sorted(set2), sep=", ")
