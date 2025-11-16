a=int(input("Enter the length of base of triangle:"))
b=int(input("Enter the length of side of triangle:"))
c=int(input("Enter the length of side of triangle:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
if(area==0):
    print("The three vertices are collinear.")
else:
    print("Area of triangle is : ",area)
