balance = 1000
amount = int(input())

if amount <= 0 :
    print("Invalid amount")
elif amount > balance :
    print("insufficient balance")
else : 
    print("Your balance is",balance - amount)