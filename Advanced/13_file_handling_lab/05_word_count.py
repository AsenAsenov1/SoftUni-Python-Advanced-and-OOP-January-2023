"""
Write a program that reads a list of words from the file words.txt and finds how many times each of the words is
contained in another file text.txt. Matching should be case-insensitive.
The results should be written to other text files. Sort the words by frequency in descending order
"""

import re

words_count = {}
words_list = []

# Open words.txt and create initial list and dictionary with the words that will be searched
with open("./words.txt", "r") as words:
    words_list.extend(words.readline().split())
    for word in words_list:
        words_count[word] = 0

# Open input.txt
with open("./input.txt", "r") as text:
    input_file = text.read().lower()

    # Find and count all the specific words and add them to dictionary
    for word in words_list:
        found_words = re.findall(rf"\W{word}\W", input_file)
        words_count[word] = len(found_words)

#  Create new text file and write output data in it
with open("./output.txt", "x") as output:
    for word, count in sorted(words_count.items(), key=lambda x: -x[1]):
        output.write(f"{word} - {count}\n")
