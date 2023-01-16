number = int(input())

odd_set = set()
even_set = set()

for row in range(1, number + 1):
    name = input()
    char_sum = 0
    for character in name:
        char_sum += ord(character)
    char_sum //= row
    if char_sum % 2 == 0:
        even_set.add(char_sum)
    else:
        odd_set.add(char_sum)

odd_set_sum = sum(odd_set)
even_set_sum = sum(even_set)

if odd_set_sum == even_set_sum:
    result = odd_set.union(even_set)
elif odd_set_sum > even_set_sum:
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)

print(", ".join(list(map(str, result))))
