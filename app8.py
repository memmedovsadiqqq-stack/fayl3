price = int(input("Enter the price: "))

if price >= 100 and price < 300:
    print(price * 0.9)
elif price < 500:
    print(price * 0.85)
elif price >= 500:
    print(price * 0.8)
else:
    print("No discount")