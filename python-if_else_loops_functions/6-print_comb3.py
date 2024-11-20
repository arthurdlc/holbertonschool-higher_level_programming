#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:  # Dernière combinaison
            print(f"{i}{j}")
        elif i < 8 or j < 9:  # Toutes les combinaisons sauf la dernière
            print(f"{i}{j}", end=", ")
