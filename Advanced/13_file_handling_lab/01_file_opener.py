"""
You are given a file called text.txt with the following text:

Create a program that opens the file. If the file is found, print 'File found'. If the file is not found, print 'File not found'.
"""

import os

path = "./text.txt"

if os.path.exists(path):
    print("File found")
else:
    print("File not found")
