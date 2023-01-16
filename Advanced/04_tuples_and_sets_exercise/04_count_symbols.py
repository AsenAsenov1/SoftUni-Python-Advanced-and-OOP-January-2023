text = input()

counter = {char: text.count(char) for char in text}

for char, count in sorted(counter.items()):
    print(f"{char}: {count} time/s")
