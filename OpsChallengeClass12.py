#!/usr/bin/env python3

# Script: Python Requests Library
# Author: Renona Gay
# Date: 12/17/2023

import requests

# Prompt user for URL
url = input("Enter destination URL: ")

# Show menu and get user choice for HTTP method
methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
print("Select HTTP method:")
for i, method in enumerate(methods):
    print(f"{i+1}. {method}")

# This block checks if the user made a valid choice.
try:
    method_choice = int(input()) - 1
    method = methods[method_choice]
except ValueError:
    print("Invalid selection. Please enter a number between 1 and 7.")
    exit()

# Block for printing the request details and confirming with user
print(f"\nPreparing request:")
print(f"  URL: {url}")
print(f"  Method: {method}")
print("Press Enter to continue or Ctrl+C to cancel.")
input()

# Send the request to website that user typed in, with the chosen method using requests library
response = requests.request(method, url)

# Translates and prints response status code
status_code = response.status_code
status_msg = {
    200: "OK",
    301: "Moved Permanently",
    302: "Found (Redirected)",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    500: "Internal Server Error",
}.get(status_code, f"Unknown error ({status_code})")

print(f"\nResponse status: {status_msg}")

# Print responses 
print("\nResponse headers:")
for key, value in response.headers.items():
    print(f"  {key}: {value}")


