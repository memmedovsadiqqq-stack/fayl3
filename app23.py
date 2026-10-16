amount = 1000
pin = "0427"
PIN = input("Enter your PIN: ")
AMOUNT = int(input("Enter the amount to withdraw: "))

if PIN.isdigit() and len(PIN) == 4 and PIN == pin and 0 < AMOUNT <= amount:
    fee = 0 if AMOUNT <= 200  else 2
    amount -= (AMOUNT + fee)
if amount >= 0 :
    print(f"Transaction successful. Remaining balance: {amount}")
else:
    print("Invalid PIN or insufficient funds.")