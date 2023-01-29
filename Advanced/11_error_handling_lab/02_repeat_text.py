"""
Write a program that receives a text on the first line and times (to repeat the text) that must be an integer.
If the user passes a non-integer type for the times variable, handle the exception and print a message
"Variable times must be an integer".
"""


def repeat(text_str: str, repeat_times: int):
    return text_str * repeat_times


try:
    text = input()
    times = int(input())
    print(repeat(text, times))

except ValueError:
    print("Variable times must be an integer")
