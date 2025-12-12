#Write a program to print sum of digits.
a=input("Enter a number :")
n=len(a)
a=int (a)
b=0
c=0
d=a
for i in range(0,n):
    b=d%10
    #print(b)
    c=c+b    
    #print(c)
    d=d//10
    #print(d)
print(f"The sum is {c}.")