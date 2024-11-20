#!/usr/bin/python3
for i in range(1, 101):  # Itération de 1 à 100
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")  # Print FizzBuzz si divisible par 3 et 5
    elif i % 3 == 0:
        print("Fizz", end=" ")  # Print Fizz si divisible par 3
    elif i % 5 == 0:
        print("Buzz", end=" ")  # Print Buzz si divisible par 5
    else:
        print(i, end=" ")  # Print le nombre si non divisible par 3 ou 5
