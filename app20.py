ID = input("Enter your ID: ")

if ID.isdigit() and len(ID) == 8:
    print("Valid ID.")
else:
    print("Invalid ID. ")