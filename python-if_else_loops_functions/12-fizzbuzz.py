#!/usr/bin/python3
for i in range(101):  # Corrected to use parentheses
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  # Print FizzBuzz if divisible by both 3 and 5
    elif i % 3 == 0:
        print("Fizz")  # Print Fizz if divisible by 3
    elif i % 5 == 0:
        print("Buzz")  # Print Buzz if divisible by 5
    else:
        print(i)  # Print the number if not divisible by 3 or 5
