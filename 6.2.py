#Create a tuple to store n numeric values and find average of all values.
n=int(input("Enter the value of n"))
c=()
d=[]
for i in range(0,n):
    b=int(input("Enter:"))
    d.append(b)
    c=tuple(d)
print(c)
print("sum:",sum(c)/n)