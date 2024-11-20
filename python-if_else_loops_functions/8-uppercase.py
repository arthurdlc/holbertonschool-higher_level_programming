#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:  # Check if the character is a lowercase letter
            result = chr(ord(char) - 32)  # Convert to uppercase by subtracting 32 from ASCII value
        else:
            result += char  # Keep the character unchanged if it's not lowercase
    print(result)  # First print function to output the result
