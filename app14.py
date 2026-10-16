a = int(input())
b = int(input())
c = int(input())

if a + b > c and b + c > a and a + c > b :
    if a == b and b == c :
        print("Equilateral")
    elif a == c or a == b or b == c :
        print("Isosceles")
    else :
        print("Scalene")
else :
    print("Triangle cannot be created")