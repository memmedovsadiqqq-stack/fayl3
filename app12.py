distance = int(input("Enter the distance: "))
fee = 2

if distance <= 5:
    fee = fee + distance * 0.7
    print(fee)
elif distance <= 15:
    fee = fee + (5 * 0.7) + ((distance - 5) * 0.6)
    print(fee)
elif distance > 15:
    fee = fee + (5 * 0.7) + (10 * 0.6) + ((distance - 15) * 0.5)
    print(fee)
else : 
    print("Invalid distance input.")