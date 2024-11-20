#!/usr/bin/python3
for i in range(10):  # Outer loop for the first digit
    for j in range(i + 1, 10):  # Inner loop for the second digit
        if i == 8 and j == 9:  # Last combination
            print(f"{i}{j}")
        else:
            print(f"{i}{j}", end=", ")  # Print with comma and space
