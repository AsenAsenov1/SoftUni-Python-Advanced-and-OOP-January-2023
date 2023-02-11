"""
Create a module that can create a Fibonacci sequence up to a number (count of numbers in the sequence) and print them,
separating them with a single space. The module should also be able to locate a specific number in the sequence.
You can read more about the Fibonacci sequence here: https://en.wikipedia.org/wiki/Fibonacci_number
You will be receiving commands until the "Stop" command. The commands are:
•	"Create Sequence {count}". Create a series of numbers up to a specific count and print them in the following format:
           "{n1} {n2} … {n}"

•	"Locate {number}"
Check if the sequence contains the number. If it finds the number, it should print:
"The number - {number} is at index {index}"
And if it doesn't find it:
"The number {number} is not in the sequence"

Input:
Create Sequence 10
Locate 13
Create Sequence 3
Locate 10
Stop

Output:
0 1 1 2 3 5 8 13 21 34
The number - 13 is at index 7
0 1 1
The number 10 is not in the sequence

"""

from fibonacci import fib_create, fib_locate


def main():
    fib_list = []

    while True:
        input_line = input()
        if input_line == "Stop":
            break

        split_data = input_line.split()
        command, number = split_data[0], int(split_data[-1])

        if command == "Create":
            fib_list = fib_create(number)
            print(*fib_list)
        elif command == "Locate":
            print(fib_locate(number, fib_list))


if __name__ == main():
    main()
