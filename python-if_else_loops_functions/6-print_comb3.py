#!/usr/bin/python3

for i in range(10):  # Première boucle : i va de 0 à 9
    for j in range(i + 1, 10):  # Deuxième boucle : j commence à i+1 pour éviter les répétitions
        if i == 8 and j == 9:  # Cas particulier pour la dernière combinaison
            print(f"{i}{j}")
        else:
            print(f"{i}{j}", end=", ")  # Ajoute une virgule et un espace
