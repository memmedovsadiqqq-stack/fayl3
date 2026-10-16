symbol = input()
a = int (input())
b = int (input())

if symbol == "+" :
    print(a+b)
elif symbol == "-" :
    print(a-b)
elif symbol == "*" :
    print(a*b)
elif symbol == "**" :
    if a == 0 and b < 0:
        print("wrong operation")
    else:
        print(a**b)
elif b == 0 :
    print("wrong operation")
elif symbol == "/" :
    print(a/b)
elif symbol == "//" :
    print(a//b)
elif symbol == "%" :
    print(a%b)