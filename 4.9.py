prime=[]
composite=[]
all=[]
#print("1")
for a in range(2,101):
    for i in range(2,a):
        if(a%i==0):
            n=1
            composite.append(a)
            break
for i in range(2,101):
    if i not in composite:
        prime.append(i)
print(f"Prime numbers:\n---{prime}\n\n")
print(f"Composite numbers:\n---{composite}")            