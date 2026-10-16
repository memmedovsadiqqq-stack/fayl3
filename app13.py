age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))
loan_amount = int(input("Enter the loan amount: "))

if age < 0 or salary < 0 or loan_amount < 0:
    print("Invalid input. Age, salary, and loan amount must be non-negative.")  
elif age < 18:
    print("You are not eligible for a loan due to age restrictions.")
elif salary < 500:
    print("You are not eligible for a loan due to insufficient salary.")
elif loan_amount > salary * 10:
    print("You are not eligible for a loan as the requested amount exceeds 10 times your salary.")
else:
    print("You are eligible for the loan.")