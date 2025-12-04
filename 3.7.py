print("Enter the value of date month and year:")
d=int(input())
m=int(input())
a=int(input())
print(d,m,a,sep="/")
err=0
if(a%400==0):
    l=1
elif(a%4==0):
    l=1
else:
    l=0
if(m>12):
    err+=1
if m in(1,3,5,7,9,11):
    date=31
    if(d>31):
        err+=1
elif m == 2:
    if (l==1):
        date=29
        if(d>29):
            err+=1
    else:
        date=28
        if(d>28):
            err+=1
elif(4,6,8,10,12):
    date=30
    if(d>31):
        err+=1
else:
    print("Not valid")
if err==0:
    if (d<date):
        d+=1
    else:
        d=1
        if m==12:
            m=1
            a+=1
        else:
            m+=1
    print("Next date is ",d,m,a,sep=":")
else:
    print("No such date.")