'''student=(1,"Sarang","First_year",86.5)
print(student)
roll=(1,3,4,5)
print(type(roll))
first=(1,2,3)
second=(4,5,6)
print("len(first)",len(first))
print("minimum:",min(first))
print(first and second)
print(first*3)
print(student[1])
list=[]
b=[2,3,4,5,56]
print(b[2])
mylist=["lion","african","dodo","length"]
print(len(mylist))
print(mylist[1])
print(mylist[0:5:2])
print(mylist[::])
mylist[2]="apple"
print(mylist)
my_tuple=(1,2,3,4)
print(my_tuple*2)
mylist.remove()
print(mylist)
##dictionary
d={1:'value','key':2}
print(d[])
s={"hello",2,2,3,4,5,"blah","2.rt"}
print(type(s))
for i in s[]:
    print(i)
dict={"a":"ford",
      "model":"mustang",
      "year":1234,
      "year":1222}
print(dict["year"])
a=dict(name="H",age=20,college="upes")
print(a)
s={"apple","banana","car","apple",0,True,1,2,False,0}
print(s)
s=set((1,2,3,4,5,"Aple")
tim="5"
print("there are"+tim+"hours")
mystery=7_45.123
print(type(mystery))
a="apple"
print(a[4]+a[3])
score=0
h=1.8
ise=True
print(f"your score is {score},your height is {h},you are winning{ise}")
name="john"
age=25
#format string using % operator
#print("%s is %d years old"%(name,age))
#format()method
print("{} is {} years old".format(name,age))'''
'''name=input("Enter Name:")
if name.lower()=="narind":
    print("Hello Narind Good Morning")
print("How are you!!!")
a=1
b=0
print("")
a=('a','b','a','c')
print(a.remove('a'))
m={2,3,4}
#print(m.pop())
print(m.clear())
employees = {}
for i in range(3):
    name = input("Enter employee's name: ")
    salary = input("Enter employee's salary: ")
    employees[name] = salary
# 👇️ {'Alice': '100', 'Bob': '100', 'Carl': '100'}
print(employees)
                                                         #2/5/2024
str="Welcome to python"
for i in str:
    print(i,end=" ")
print(str.upper)
a="+".join(str.split())
print(type(a),a)
print(str.replace("python", "java"))
a=[]
i=0
while True:
    print(chr(i),end=" ")
    i=i+1
import string
print("g" in string.ascii_lowercase)
a=input("Enter a number:")
n=len(a)
a=int (a)
b=0
c=0
d=a
for i in range(1,n+1):
    b=d%10
    c=c+b*10**(n-i)
    d=d//10
    print(c)
if c==a:
    print(f"{a} is a palindrome.")
else:
    p(rint(f"{a} is not a palindrome")
a=[1,2,3,4,5,5]
for i,index in enumerate(a):
    print(index,"is at index:",i)
b=iter(a)
print(b)
for i in range(len(a)):
    print("Element at index",i,"is :",next(b))
    print(b)
                                                        9th february 2024
planet='earth'
diameter=12345
print(f"The diameter of {planet} is {diameter} kilometers")
print("The diameter of {} is {} kilometers".format (planet,diameter))
list=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(list[3][1][2][0])
d={'k1':[1,2,3,{'trickey':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['trickey'][3]['target'][3])
def domain(a):
    c=a.split("@")
    print(str(c[1]))

a=input("Enter a mail:")
b=domain(a)
def find(a,b):
    if b in a:
        return True
    else:
        return False
a=input("Enter a string")
b=input("Enter:")
print(find(a,b))
def display(*q):
    print(q)
tup=(1,2,3,4,5,56,7,)
display(tup)
a=(1,2,3,4)
l=[1,2,3,4,5]
print(list((zip(a,l))))
print(dict(zip(a,l)))
d={'roll_no':'16/001','name':'arav','corse':'btech'}
print("dict[rollnumber]",d['roll_no'],"dict[name]",d['name'])
print("dict[course]=",d['corse'])
#d['marks']=95
#print("dict[marks]=",d['marks'])
print(d)
print('marks is:',d.pop('marks',0))
print("after randomly popping the dict is:",d.popitem())
students={'shiv':{'cs':90,'ds':89,'csa':89},
          'a':{'cs':95,'ds':90,'csa':95},
          'c':{'cs':92,'ds':91,'csa':93}}
for key,val in students.items():
    print(key,val)'''
