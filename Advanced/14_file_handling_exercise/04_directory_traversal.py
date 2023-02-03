"""
Write a program that traverses a given directory for all files. Search through the first level of the directory only and
 write information about each found file in report.txt. The files should be grouped by their extension.
 Extensions should be ordered by name alphabetically. The files with extensions should also be sorted by name.
 report.txt should be saved in the chosen directory.
"""

from os import listdir

path = "./"
found_files = listdir(path)
extension_dict = {}

for file in found_files:
    extension = "." + file.split(".")[1]

    if extension not in extension_dict:
        extension_dict[extension] = []

    extension_dict[extension].append(file)

with open("./report.txt", "w") as report:
    for extension_type, filenames in sorted(extension_dict.items(), key=lambda x: x[0]):
        report.write(extension_type + "\n")

        for item in filenames:
            report.write("- - - " + item + "\n")
