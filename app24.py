product_code = input("Enter product code: ").upper
quantity = input("Enter quantity: ")
coupon_code = input("Enter coupon code : ")
delivery_code = input("Enter delivery code: ")

match product_code:
    case "K":
        price = 40
    case "M":
        price = 20
    case "H":
        price = 60
    case _:
        print("Invalid product code.")
        price = 0
if  quantity.isdigit() and int(quantity) > 0 and int(quantity) <= 5 :
    total_price = price * int(quantity)
else:
    print("Invalid quantity. Please enter a number between 1 and 5.")
    total_price = 0
if coupon_code == "SAVE10":
    total_price *= 0.9
elif coupon_code == "NONE":
    total_price *= 1
else:
    print("Invalid coupon code. No discount applied.")
match total_price:
    case total_price if total_price < 80 :
        delivery_fee = 5
    case total_price if total_price >= 80 :
        delivery_fee = 0
total_price += delivery_fee
if total_price > 0 and total_price != 5 :
    print("Total price: {total_price}")
else :
    print("Order could not be processed due to invalid inputs.")