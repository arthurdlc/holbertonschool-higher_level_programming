#!/usr/bin/python3

def fizzbuzz():
    result = []  # Créer une liste pour stocker les résultats
    for i in range(1, 101):  # Boucle de 1 à 100
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")  # Ajouter "FizzBuzz" pour les multiples de 3 et 5
        elif i % 3 == 0:
            result.append("Fizz")  # Ajouter "Fizz" pour les multiples de 3
        elif i % 5 == 0:
            result.append("Buzz")  # Ajouter "Buzz" pour les multiples de 5
        else:
            result.append(str(i))  # Ajouter le nombre lui-même s'il n'est pas un multiple

    print(" ".join(result))  # Joindre les résultats avec des espaces et les imprimer
