with open('name.txt','w')as file:
    name=['appleerfewrfwerfer\n',
'APPLE\n',
'BANANA\n',
'PEACHES\n',
'GUAVA\n',
'PINE\n',
'PINEAPPLE\n',
'GRAPES']
    file.writelines(name)
v='aeiouAEIOU'
with open('name.txt','r')as file:
    a=file.readlines()
    print(len(a))
    c=0
    for i in a:
        if i.strip()[0] in v:
            c +=1
    print("Number of name starting with vowels:",c)
    for i in a:
        if i==max(a):
            print(i)