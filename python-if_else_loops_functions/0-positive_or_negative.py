#!/usr/bin/python3
from random import randint

number = randint

if number < 0:
	print(number, "is negative")
elif number == 0:
	print(number, "is zero")
else:
	print(number, "is positive")
