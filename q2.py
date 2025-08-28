t1=(1,2,3,4,5)
t2=(2,3,4,5)
j=0
for i in range(0,5):
    if t1[i] in t2[j] :
        print(t1[i])
        j+=1
    else:
        continue