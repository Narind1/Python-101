a=[10,2,3,4,8,11]
'''b=[]
c=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        b.append(a[i])
    else:
        c.append(a[i])
print("Max odd:",max(b))
print("Max even:",max(c))'''
b=[]
a.sort()
for i in range(0,len(0)):
    if a[i]%2!=0:
        a.pop()
    else:
        b.append(a[i])
print(b)
