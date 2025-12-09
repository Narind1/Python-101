a=int(input("Enter a number:"))
n=0
for i in range(2,a):
    if(a%i==0):
        n=n+1
        break
if n>0:
    print(f"{a} is composite")
elif(a==1):
    print("1 is neither prime nor composite.")
else:
    print(f"{a} is prime")