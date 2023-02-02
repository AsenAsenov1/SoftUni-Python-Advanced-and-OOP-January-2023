"""
Create a program that deletes the file you created in the previous task.
If you try to delete the file multiple times, print the message: 'File already deleted!'.
"""

import os

filename = 'my_first_file.txt'

if os.path.exists(filename):
    os.remove(filename)
else:
    print('File already deleted!')
