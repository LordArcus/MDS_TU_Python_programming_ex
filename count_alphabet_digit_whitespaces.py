# Write a program to count number of alphabets, digits, and whitespaces in a string.

string = input("Enter a string: ")
alphabet_count = 0
digit_count = 0
whitespace_count = 0
for char in string:
    if char.isalpha():
        alphabet_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        whitespace_count += 1
print("Number of alphabets:", alphabet_count)
print("Number of digits:", digit_count)
print("Number of whitespaces:", whitespace_count)