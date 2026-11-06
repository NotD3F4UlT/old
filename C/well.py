x=int(input("first number:"))
y=int(input("second number:"))
z=input("operator:")

if z in ("+","-","*","/"):
    if z=="+":
        print(x+y)
    elif z=="-":
        print(x-y)
    elif z=="*":
        print(x*y)
    elif z=="/":
        if y==0:
            print("Undefined")
        else:
            print(x/y)
else:
    print("invalid operator")