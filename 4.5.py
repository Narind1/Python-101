#Check whether given number is palindrome or not.
a=input("Enter a number:")
n=len(a)
a=int (a)
b=0
c=0
d=a
for i in range(1,n+1):
    b=d%10
    #print(b)
    c=c+b*10**(n-i)
    #print(c)
    d=d//10
    #print(d)
if c==a:
    print(f"{a} is a palindrome.")
else:
    print(f"{a} is not a palindrome")