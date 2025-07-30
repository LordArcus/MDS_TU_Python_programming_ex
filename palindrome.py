# Write a program to check whether a number is palindrome or not.

number = input("Enter a number: ")
is_palindrome = number == number[::-1]
if is_palindrome:
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")