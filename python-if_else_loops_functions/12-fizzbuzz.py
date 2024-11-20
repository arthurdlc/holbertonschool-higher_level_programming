#!/usr/bin/python3
for i in range(1, 101):  # Itération de 1 à 100
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()  # Ajoutez cette ligne pour s'assurer qu'il y a une nouvelle ligne après la dernière valeur
