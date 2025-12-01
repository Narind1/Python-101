a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
if (a>=b)& (a>=c):
    print("A is greatest")
elif (b>=a) & (b>=c):
    print("B is greatest.")
elif (c>=a) & (c>=b):
    print("C is greatest.")
else:
    print("Enter different values.")