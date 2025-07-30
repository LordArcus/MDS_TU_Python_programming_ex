# Write a program to check if a number is Armstrong Number or not.

number = int(input("Enter a number: "))
sum_of_powers = 0
temp = number
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** 3
    temp //= 10
if sum_of_powers == number:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")