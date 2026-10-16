PIN = input("Enter your PIN: ")
pin1 = "0427"

if PIN.isdigit() and len(PIN) == 4 and PIN == pin1:
    print("Valid PIN.")
else:
    print("Invalid PIN. Please enter a 4-digit numeric PIN.")