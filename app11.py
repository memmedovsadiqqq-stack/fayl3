usage = int(input("Enter the usage: "))

if usage <= 100:
    bill = usage * 0.8
    print(bill)
elif usage <= 300:
    bill = (100 * 0.8) + ((usage - 100) * 0.12)
    print(bill)
elif usage > 300:
    bill = (100 * 0.8) + (200 * 0.12) + ((usage - 300) * 0.15)
    print(bill)
else :
    print("Invalid usage input.")