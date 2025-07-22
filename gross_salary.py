# The rates of tax on gross salary are as shown below:

# Less than 10,000 Nill
# Rs. 10,000 to 19,999 10%
# Rs. 20,000 to 39,999 15%
# Rs. 40,000 to above 20%

#Write a program to compute the net salary after deducting the tax for the given information
#and print the same.

gross_salary = float(input("Enter the gross salary: "))
if gross_salary < 10000:
    tax = 0
elif 10000 <= gross_salary < 20000:
    tax = 0.10 * gross_salary
elif 20000 <= gross_salary < 40000:
    tax = 0.15 * gross_salary
else:
    tax = 0.20 * gross_salary       

net_salary = gross_salary - tax
print("The net salary is:", net_salary)
