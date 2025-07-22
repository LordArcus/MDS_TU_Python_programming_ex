# Write a program to calculate discount on the basis of following assumption:

# If purchased amount is greater than or equal to 5000, discount is 10%
# If purchased amount is greater than or equal to 4000 and less than 5000, discount is 7%
# If purchased amount is greater than or equal to 3000 and less than 4000, discount is 5%
# If purchased amount is greater than or equal to 2000 and less than 3000, discount is 3%
# If purchased amount is less than 2000, discount is 2%


purchased_amount = float(input("Enter the purchased amount: "))
if purchased_amount >= 5000:
    discount = 0.10 * purchased_amount
elif purchased_amount >= 4000:
    discount = 0.07 * purchased_amount
elif purchased_amount >= 3000:
    discount = 0.05 * purchased_amount
elif purchased_amount >= 2000:
    discount = 0.03 * purchased_amount
else:
    discount = 0.02 * purchased_amount
print(f"The discount is {discount}.")