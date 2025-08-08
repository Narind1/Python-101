#paint area h,w,l
def paintarea(h,w,l):
    area=4*(h*w)+l*w
    pta=area//4
    print("Number of cans required:",pta)
    print("area:",area)
a=int(input("Enter the height:"))
b=int(input("Enter the width:"))
c=int(input("Enter the length:"))
paintarea(a,b,c)