"""
Write a program that reads a text file, inserts line numbers in front of each line,
and counts all the letters and punctuation marks. The result should be written to another text file.
"""
import re

text_file = "./text.txt"
letters_pattern = r"[A-Za-z]"
punctuation_pattern = r"[^\w\s]"
saved_data = []

with open(text_file, 'r') as file:
    for index, line in enumerate(file):
        index += 1
        found_letters = len(re.findall(letters_pattern, line))
        found_punctuation = len(re.findall(punctuation_pattern, line))

        write_line = f"Line {index}: {line.strip()} ({found_letters})({found_punctuation})"
        saved_data.append(write_line)

with open("./output.txt", 'w+') as output_file:
    for line in saved_data:
        output_file.write(line + '\n')

