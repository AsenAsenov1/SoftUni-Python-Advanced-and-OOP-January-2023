"""
You are given a file called numbers.txt with the following content:
1
2
3
4
5

Create a program that reads the numbers from the file. Print on the console the sum of those numbers.
"""

with open("./numbers.txt", "r") as text_file:
    total_sum = 0
    for num in text_file:
        total_sum += int(num)
    print(total_sum)
