#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)

last_digit = abs(number) % 10

if last_digit > 5:
    f"Last digit of {number} is {last_digit} and is greater than 5"
elif last_digit == 0:
    f"Last digit of {number} is {last_digit} and is 0"
else last_digit < 6 and last_digit != 0:
    f"Last digit of {number} is {last_digit} and is less than 6 and not 0"
