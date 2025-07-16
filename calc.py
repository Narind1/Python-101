from art import logo
def add(a,b):
    return (a+b)
def dif(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return(a/b)
op={
    "+":add,"-":dif,"x":mul,"/":div
}
print(logo)
while (1):
    print("Enter two numbers:")
    a=int(input())
    b=int(input())
    print("Enter an operation: +,-,x or / : ")
    opr=input()
    if opr not in op.keys():
        print("Invalid Operator")
    else:
        print(f"{a}{opr}{b} = {op[opr](a,b)}")
        c=input("Do you want to continue:\ny/n:")
        if  c=="n":
            print("Thank you for using my calculator:")
            break
        else:
            continue
    
#ask user if he wants to continue or not