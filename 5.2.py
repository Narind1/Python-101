vowels="'a','e','i','o','u','A','E','I','O','U'"
a=input("Enter a string:")
c=0
for i in range(0,len(a)):
    if a[i] in vowels:
        c+=1
print("Total vowels:",c)