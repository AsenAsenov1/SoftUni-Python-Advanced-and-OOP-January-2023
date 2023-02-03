"""
Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0.
Before you print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.
"""

text_file = "./text.txt"
symbols = {"-", ",", ".", "!", "?"}
stored_lines = []

with open(text_file, 'r') as file:
    for index, line in enumerate(file):
        if index % 2 == 1:
            continue

        for symbol in symbols:
            if symbol in line:
                line = line.replace(symbol, "@")

        new_line = line.split()
        stored_lines.append(new_line[::-1])

[print(*x) for x in stored_lines]
