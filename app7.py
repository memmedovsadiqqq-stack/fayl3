age = int(input())

if age < 0 :
    print("Invalid age")
elif age >= 65 :
    print("senior")
elif age >= 18 :
    print("adult")
elif age >= 13 :
    print("teenager")
else :
    print("child")