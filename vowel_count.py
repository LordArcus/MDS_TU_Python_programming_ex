# Write a program to count number of vowels in a string.

string = input("Enter a string: ")
vowel_count = 0
for char in string.lower():
    if char in "aeiou":
        vowel_count += 1
print("Number of vowels:", vowel_count)
