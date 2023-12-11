#!/usr/bin/env python3

# Line telling Python to use the "os" library for file handling.

import os

# This line defines the path and name of the text file.

file_path = "my_file.txt"

# This line uses the "open" function to create a new file.
# Must pecify "w" for writing mode.
with open(file_path, "w") as file:

    # This line adds the first line to the file.

    file.write("This is the first line.\n")

    # This line adds the second line to the file.

    file.write("This is the second line.\n")

    # This line adds the third line to the file.

    file.write("This is the third line.")

# Open the file again in reading mode.

with open(file_path, "r") as file:

    # Read the first line of the file.

    first_line = file.readline()

    # Print the first line to the screen.

    print(first_line)

    # Use the "os.remove" function to delete the text file.

os.remove(file_path)

Resources used: https://g.co/bard/share/394efc0e7fa3
