"""
Write a program that encrypts given words by using the characters: "-|_/\()" to structure the word.
Use the pyfiglet module.
"""

from pyfiglet import figlet_format


def print_msg(message):
    return figlet_format(message)


print(print_msg(input()))
