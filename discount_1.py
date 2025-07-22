# Write a program to calculate discount on the basis of following assumption:

# If purchased amount is greater than or equal to 1000, discount is 5%

purchased_amount = float(input("Enter the purchased amount: "))
if purchased_amount >= 1000:
    discount = 0.05 * purchased_amount
else:
    discount = 0
print(f"The discount is {discount}.")