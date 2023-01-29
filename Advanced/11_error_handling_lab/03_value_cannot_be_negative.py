"""
Create your own exception called ValueCannotBeNegative.
Write a program that reads five numbers from the console (on separate lines).
If a negative number occurs, raise the exception.
"""


class ValueCannotBeNegative(Exception):
    pass


numbers = []
for _ in range(5):
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueCannotBeNegative("Negative number entered")
    numbers.append(num)

print("Numbers entered:", numbers)
