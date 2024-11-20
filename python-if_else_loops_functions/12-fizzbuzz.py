#!/usr/bin/python3

def fizzbuzz():
    result = []  # Create a list to hold the results
    for i in range(101):  # Loop from 0 to 100
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")  # Append "FizzBuzz" for multiples of both
        elif i % 3 == 0:
            result.append("Fizz")  # Append "Fizz" for multiples of 3
        elif i % 5 == 0:
            result.append("Buzz")  # Append "Buzz" for multiples of 5
        else:
            result.append(str(i))  # Append the number itself if not a multiple

    print(" ".join(result) + " $")  # Join the results with spaces and print with a trailing dollar sign

# Call the fizzbuzz function
fizzbuzz()
