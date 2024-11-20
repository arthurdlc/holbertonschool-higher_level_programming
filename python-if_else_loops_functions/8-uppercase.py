#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:  # Check if char is lowercase
            result += chr(ord(char) - 32)  # Convert to uppercase
        else:
            result += char  # Keep unchanged if not lowercase
    print("{}".format(result))  # Print the result
