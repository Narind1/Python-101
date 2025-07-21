def encrypt(a,b):
    c=a
    letters=[]
    for i in range (65,91) or (97,124):
        letters.append(chr(i))
    for i in range(0,len(letters)):
        for j in range(0,len(a)):
            if letters[i]==c[j]:
                a.replace(c[j],letters[i+b])
            else:
                continue
    print("jfy")
a=input("Enter a string:")
b=int(input("Enter the shift:"))
encrypt(a,b)