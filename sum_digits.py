# Write a program to find sum of digits of a number.

number = int(input("Enter a number: "))
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10
print("Sum of digits:", sum_of_digits)