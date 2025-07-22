# Write a program to calculate discount on the basis of following assumption:

# If purchased amount is greater than or equal to 1000, discount is 5%

# If purchased amount is less than 1000, discount is 3%

purchased_amount = float(input("Enter the purchased amount: "))
if purchased_amount >= 1000:
    discount = 0.05 * purchased_amount
else:
    discount = 0.03 * purchased_amount
print(f"The discount is {discount}.")