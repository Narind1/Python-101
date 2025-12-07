a=input("Enter a number:\n--")
n=len(a)
a=int (a)
c=0
d=0
e=a
for i in range(0,n):
    d=e % 10
    b=d**n
    c=c+b
    e=e//10
if (c==a):
    print(f"{a} is an armstrong number")
else:
    print(f"{a} is not armstrong number")