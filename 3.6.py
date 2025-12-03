#find leap year or not
a=int(input("Enter a year:"))
if(a%400==0):
    print(a,"is a leap year")
elif(a%4==0):
    print(a,"is a leap year")
else:
    print(a,"is not a leap year.")