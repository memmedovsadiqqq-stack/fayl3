phone_number = input("Enter your phone number: ")

if phone_number.isdigit() and len(phone_number) == 10:
    if phone_number.startswith("050") or phone_number.startswith("051") or phone_number.startswith("052") or phone_number.startswith("055") or phone_number.startswith("070") or phone_number.startswith("077"):
        print("Valid phone number.")
    else:
        print("Invalid phone number. Please enter a valid prefix.")