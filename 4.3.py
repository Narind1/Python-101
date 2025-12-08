n=int(input("Enter the range of series:\n---"))
series=0
num1=0
num2=1
print(f"The fibonacci series upto {n} terms is:")
for i in range(0,n):
    print(num1,end="  ")
    series=num1+num2
    num1=num2
    num2=series