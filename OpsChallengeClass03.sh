#!/bin/bash

# Prompt for directory path
read -p "Enter any directory path: " dir

# Prompt for permissions number
read -p "Enter permissions number: " permissionsNum

# Prompt for changing the directory as specified by the user
cd $dirPath

# For loop to iterate through all files within directory; using a "for" loop to process each file
for file in *; do 
    # Process each file
done

# Using chmod to change permission of each file to a number specified by user
chmod $permissionsNum "$file"

# Using the ls command to list contents of the directory, including the modified permissions
ls -l

# Resources used: https://g.co/bard/share/682b3b316fc6