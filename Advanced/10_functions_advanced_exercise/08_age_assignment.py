def age_assignment(*args, **kwargs):
    names = {}
    for character, age in kwargs.items():
        for name in args:
            if name.startswith(character):
                names[name] = age
    sorted_names = [f"{name} is {age} years old." for name, age in sorted(names.items())]

    return "\n".join(sorted_names)


print(age_assignment("Peter", "George", G=26, P=19))
# Output:
# George is 26 years old.
# Peter is 19 years old.
print()

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
# Output:
# Amy is 22 years old.
# Bill is 61 years old.
# Willy is 36 years old.
