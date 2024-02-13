purchase = float(input("Enter purchase value: "))

if purchase > 10000:
    discount = purchase * 0.5
    print("Discount is: ", discount)
elif 5000 < purchase <= 10000:
    discount = purchase * 0.3
    print("Discount is: ", discount)
elif 1000 < purchase <= 5000:
    discount = purchase * 0.2
    print("Discount is: ", discount)
else:
    discount = purchase * 0.1
    print("Discount is: ", discount)

