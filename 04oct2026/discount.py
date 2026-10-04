price = int(input("Enter the price: "))
discount = int(input("Enter thr discount: "))

discount_amount = (discount/100)*price

print(f"discount amount: {discount_amount}")
print(f"finial price: {price-discount_amount}")