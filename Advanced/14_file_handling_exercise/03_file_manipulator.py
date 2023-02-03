"""
Create a program that will receive commands until the command "End". The commands can be:
•	"Create-{file_name}" - Creates the given file with an empty content. If the file already exists,
    remove the existing text in it (as if the file is created again)
•	"Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist, create it,
    and add the content
•	"Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string
    with the new string. If the file does not exist, print: "An error occurred"
•	"Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"
"""

import os

while True:
    command = input().split("-")
    if "End" in command:
        break
    action = command[0]
    file_name = command[1]

    if action == "Create":
        with open(f"./{file_name}", "w") as file:
            pass

    elif action == "Add":
        content = command[2]
        with open(f"./{file_name}", "a+") as file:
            file.write(content + "\n")

    elif action == "Replace":
        old_string, new_string = command[2:]
        try:
            with open(f"./{file_name}", "r") as file:
                text = file.read()
                new_text = text.replace(old_string.strip(), new_string.strip())

            with open(f"./{file_name}", "w") as file:
                file.write(new_text.strip())

        except FileNotFoundError:
            print("An error occurred")

    elif action == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
