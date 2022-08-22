distance = float(input("Enter the distance"))
price = float(input("Enter the price"))
weight = float(input("Enter the weight"))
if distance < 250:
    discount = float(0)
elif 250 <= distance < 500:
    discount = float(0.1)
elif 500 <= distance < 1000:
    discount = float(0.15)
elif 1000 <= distance < 2000:
    discount = float(0.2)
elif 2000 <= distance < 3000:
    discount = float(0.35)
elif distance >= 3000:
    discount = float(0.5)
cost = float(input(price * weight * distance * (1-discount)))

print("Shipping cost", cost)
