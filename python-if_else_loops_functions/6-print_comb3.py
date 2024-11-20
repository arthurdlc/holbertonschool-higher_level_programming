#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:  # Dernière combinaison
            print(f"{i}{j}")  # Print final sans virgule ni espace
        elif i < 5:  # Combinaisons pour les premiers chiffres (0 à 4)
            print(f"{i}{j}", end=", ")
        else:  # Combinaisons pour les autres chiffres (5 à 8)
            print(f"{i}{j}", end=", ")
