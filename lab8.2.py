with open("NUM.txt",'w')as file:
    name=['100\n',
'1\n',
'101\n',
'23\n',
'45\n',
'654\n',
'34\n',
'233']
    file.writelines(name)
with open("NUM.txt",'r')as file:
    a=file.readlines()
    for i in a:
        if i==max(a):
            print(i)
    c=0
    for i in a:
        c=int(i)+c
    print(c/len(a))
    j=0
    for i in a:
        if int(i)>100:
            j+=1
    print(j)