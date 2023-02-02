import os

path = "./text.txt"

if os.path.exists(path):
    print("File found")
else:
    print("File not found")
