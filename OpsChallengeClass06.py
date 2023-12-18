#!/usr/bin/env python3


# Declare variables

username = input("What is your username? ")
ip_address = "192.168.1.100" # This is just an example, replace with your actual IP
system_info = ""

# Print welcome message with username

print(f"Hi {username}, let's explore your system!")

# Execute bash commands and store output in variables

system_info += subprocess.run(["whoami"], capture_output=True).stdout.decode("utf-8")
system_info += "\n" + subprocess.run(["ip", "a"], capture_output=True).stdout.decode("utf-8")
system_info += "\n" + subprocess.run(["lshw", "-short"], capture_output=True).stdout.decode("utf-8")

# Print information

print("\n==================== System Information ====================")
print(f"Username: {username}")
print(f"IP address: {ip_address}")
print(f"\nHardware information:")
print(system_info)

# Print goodbye message

print("\nThanks for looking at me!")

# Rescources used: https://g.co/bard/share/9036404cd2f8