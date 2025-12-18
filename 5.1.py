a=input("Enter a string:")
print("Upper case string is:")
c=0
for i in range(0,len(a)):
    '''
    if 64<ord(a[i])<91:
        print(a[i],end=" ")'''
    if a[i].isupper()==True:
        print(a[i],end=" ")
        c+=1
print("Total:",c)