#!/usr/bin/python3

for i in range(100):  # Parcourt les nombres de 0 à 99
    if i < 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))

