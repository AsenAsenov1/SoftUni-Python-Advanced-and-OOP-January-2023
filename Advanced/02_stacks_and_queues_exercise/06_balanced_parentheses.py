expression = input()

opening_brackets = []
pairs = {"(": ")",
         "[": "]",
         "{": "}"
         }
balanced = True

for character in expression:
    if character in "({[":
        opening_brackets.append(character)
    elif not opening_brackets:
        balanced = False
    else:
        last_opening_bracket = opening_brackets.pop()
        if pairs[last_opening_bracket] != character:
            balanced = False

    if not balanced:
        break

if balanced:
    print("YES")
else:
    print("NO")