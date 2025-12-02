import math
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
c=float(input("Enter value of c:"))
print("The equation is :",a,"x^2 +",b,"x +",c)
d=(b)**2-4*a*c
print("The discriminant is:",d)
if (d>0):
    print("The roots are real and distinct.")
elif (d==0):
    print("The roots are real and equal")
else:
    print("The roots are imaginary.")