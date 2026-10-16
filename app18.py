day = int(input("Enter your day: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6: 
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Enter a valid day.") 
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Study day")  
    case 6 | 7:
        print("Weekend")