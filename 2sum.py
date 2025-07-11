n=int(input("Enter the length of array:"))
b=[]
for i in range(0,n):
    a=int(input("Enter the numbers:"))
    b.append(a)
print(b)
c=int(input("Enter the target:"))
d=[]
for i in range(0,n):
    if len(d)==0:
        for j in range(0,n):
            if c==b[i]+b[j]:
                d.append(i)
                d.append(j)
print(d)