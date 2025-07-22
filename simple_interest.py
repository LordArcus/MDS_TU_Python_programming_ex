# Write a program to calculate the simple interest on the basis of following assumption:

# If balance is greater than or equal to 100000, interest is 7 %
# If balance is greater than or equal to 50000 and less than 100000 interest is 5 %
# If balance is less than 50000, interest is 3%

# The formula for simple interest is: interest = (principal * rate * time) / 100
balance = float(input("Enter the balance: "))
time = float(input("Enter the time in years: "))
if balance >= 100000:
    interest = 0.07 * balance * time
elif balance >= 50000:
    interest = 0.05 * balance * time
else:
    interest = 0.03 * balance * time
print(f"The interest is {interest}.")