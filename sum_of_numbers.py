#Write a program to find sum of two numbers using command line arguments.

import sys

if len(sys.argv) != 3:
    print("Usage: python sum_of_numbers.py <num1> <num2>")
else:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        total = num1 + num2
        print(f"The sum of {num1} and {num2} is {total}.")
    except ValueError:
        print("Please provide valid numbers.")
