#Scan n values in range 0-3 and print the number of times each value has occurred.
n=int(input("Enter the value of n"))
b=[]
for i in range(0,n):
    a=input("Enter:")
    b.append(a)
print(b)
c=0
for i in range(0,3):
    d=b.count(b[i])
    print(b[i],":",d)