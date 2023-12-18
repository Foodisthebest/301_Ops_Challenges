#!/bin/bash
# Line that tells the computer what program to use to run the script.

# This is like a loop that keeps the game running until you choose "Exit."
while true; do

# This line clears the screen, like when you start a new level.
  clear

# This shows the menu options with numbers.
# "read" asks you for your choice and stores it in the "choice" variable.
  echo "Welcome to the fun menu!"
  echo "What would you like to do?"
  echo ""
  echo "1. Hello world"
  echo "2. Ping self"
  echo "3. IP info"
  echo "4. Exit"
  echo ""
  read -p "Enter your choice: " choice

# This uses a "case" statement to check your choice:
# - 1: Prints "Hello world!"
# - 2: Pings your computer (like checking if you're connected)
# - 3: Shows your network information
# - 4: Exits the program
# - *: If you enter something else, it says "Invalid choice."

  case $choice in
    1)
      echo "Hello world!"
      ;;
    2)
      ping -c 3 127.0.0.1
      ;;
    3)
      ip addr show
      ;;
    4)
      echo "Thank you for playing!"
      break
      ;;
    *)
      echo "Invalid choice. Please try again."
      ;;
  esac


# This ends the loop when you choose "Exit."
done

