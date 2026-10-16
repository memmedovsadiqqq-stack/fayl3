total = int(input("Enter your fee: "))
membership = input("Enter your membership (yes/no): ")

if not(membership.lower() == "yes" or membership.lower() == "no") or total < 0:
    print("Enter information correctly.")
else:
    fee = 0 if membership.lower() == "yes" or total > 50 else total * 0.1
print(fee, fee + total)