!#bin/bash/

# Create an array to store menu options
options=("Hello world" "Ping self (pings this computer's loopback address)" "IP info (prints network adapter in for this computer)" "Get me out of here (Exit)")

# Create the menu loop
    # This "While" loop keeps menu displaying until user chooses the "Exit" option
while true; do

    # Sets variable "PS3" to string "Pick your choice." Prompt is shown before each menu listing; guides user to their choice
    PS3="Pick your choice: "

    # Starts a "select" loop that goes through the options array. Assigns chosen option to variable "opt"
    # "@" symbol expands the "options" array and makes each part of the array available as a seperate option
    select opt in "${options[@]}"; do

    # "case" starts a case statment handling the various menu options.
    # Vairable "$opt" has user's selection from the select loop
        case $opt in

        # Block that handles the "Hello world" option; when "Hello world" is chosen by user, "echo" prints "Hello world" on screen
        # "Break" is statment that exits case statment and select loop
            "Hello world")
                echo "Hello world!"
                break
            ;;

        # Block that handles "Ping self" option. When chosen, "ping" command pings loopback address (IP address of the computer itself)
        # Break statement exits case statement and select loop
            "Ping self")
                ping localhost
                break
            ;;

            # Block that handles "IP info" option. When chosen, "ipconfig" displays network adapter info for the computer
            # Break statement exits the case statment as well as the select loop
            "IP info")
                ifconfig
                break
            ;;

            # Block handling "Exit" option; when chosen, "exit 0" terminates script
            "Exit")
                exit 0
            ;;

            # Block handling an invalid option chosen by user. When user chooses an optoin not in the "options" array, "echo" prints error message
            *)
                echo "Invalid option: $opt"
                break
            ;;

        # End case statement    
        esac
    # End select loop    
    done
# Ends infinite loop    
done

# Resources used: https://g.co/bard/share/0fb750a43512