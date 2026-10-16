import sys

ID = input()
age = int(input())
workshop_code = input().upper
payment = input()

if ID.isdigit() == 0 or len(ID) != 8 :
    print("ID is wrong")
    sys.exit()
if age <= 16 or age >= 65 :
    print("Age inputed wrongly, try again")
    sys.exit()
match workshop_code :
    case 'PY' :
        price = 30
    case "WEB ":
        price = 40 
    case "CY" if age >=18 :
        price = 50
    case _:
        print("Wrong code")
        sys.exit
discount = 0.8 if age <=18 else 1
price1 = price * discount
if payment.isdigit() :
    payment = int(payment)
else :
    print("wrong input")
    sys.exit()
if payment <= price1 :
    print("Insufficent amount")
    sys.exit()
else :
    print("Regirstration confirmed")
    discount1 = 1 - discount 
    discount1 = price * discount1
    print(discount1)
    print(price1)
    change = payment - price1
    print(change) 