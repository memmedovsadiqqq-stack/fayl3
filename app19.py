drink_code = input("Enter your drink code (T,C,J): ").upper()
quantity = int(input("Enter your quantity: "))

if quantity >= 1 and quantity <= 10:
    match drink_code:
        case 'T':
            total_cost = 2 * quantity
            print("Total cost for {quantity} Tea(s): ${total_cost}")
        case 'C':
            total_cost = 4 * quantity
            print("Total cost for {quantity} Coffee(s): ${total_cost}")
        case 'J':
            total_cost = 3 * quantity
            print("Total cost for {quantity} Juice(s): ${total_cost}")
        case _:
            print("Invalid drink code.")
else:
    print("Invalid quantity. Please enter a value between 1 and 10.")