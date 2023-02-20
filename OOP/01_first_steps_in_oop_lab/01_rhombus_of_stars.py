""" Create a program that reads a positive integer N as input and prints on the console a rhombus with size n. """


def create_rhombus(num):
    def create_upper_half(number):
        for i in range(1, number + 1):
            print((number - i) * " " + i * " *")

    def create_lower_half(number):
        for i in range(number - 1, 0, -1):
            print((number - i) * " " + i * " *")

    create_upper_half(num)
    create_lower_half(num)


input_number = int(input())

create_rhombus(input_number)
