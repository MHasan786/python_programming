# Calculate discount based on shopping amount

shoping_amount = int(input("Enter shopping amount PKR: "))

if shoping_amount >= 4000:
    if shoping_amount >= 4000 and shoping_amount <= 6000:
        discount = 0.08 * shoping_amount
        after_discount = shoping_amount - discount
        print(f"Oringinal Amount: {shoping_amount}\nDiscount: {round(discount,2)}\nAfter Discount: {after_discount}")
    elif shoping_amount >= 6000 and shoping_amount <= 10000:
        discount = 0.12 * shoping_amount
        after_discount = shoping_amount - discount
        print(f"Oringinal Amount: {shoping_amount}\nDiscount: {round(discount,2)}\nAfter Discount: {after_discount}")
    elif shoping_amount >= 10000 and shoping_amount <= 20000:
        discount = 0.15 * shoping_amount
        after_discount = shoping_amount - discount
        print(f"Oringinal Amount: {shoping_amount}\nDiscount: {round(discount,2)}\nAfter Discount: {after_discount}")
    elif shoping_amount >=20000 and shoping_amount <= 25000:
        discount = 0.17 * shoping_amount
        after_discount = shoping_amount - discount
        print(f"Oringinal Amount: {shoping_amount}\nDiscount: {round(discount,2)}\nAfter Discount: {after_discount}")
    else:
        print("You can not avial discount.")
else:
    print("No Dicount Thanks for Shopping!")