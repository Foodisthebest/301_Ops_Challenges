#!/usr/bin/env python3

# Import libraries

import os 

# Declaration of variables
path = input("Give me a file path: ")
### Read user input here into a variable

# Declaration of functions

### Declare a function here

for (root, dirs, files) in os.walk("user_path"):
    # Print current directory 
    print("Current Directdory:", root)
    ### Add a print command here to print ==dirs==
    print("Subdirectories:", dirs)
    ### Add a print command here to print ==files==
    print("Files", files)

# Main
if __name__ == "__main__":
        generate_directory(path)
### Pass the variable into the function here

# End

# Resources used: https://github.com/iAmAndrewCarroll/Ops301/blob/main/challenges/ops7.py
# https://github.com/Z-Zachattack/Ops-301/commit/bdbbb0563ab587987ce00cff751ce09517baa3c4