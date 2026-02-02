class student:
    def __init__(self,name,sapid,phy,chem,maths):
        self.name = name
        self.sapid = sapid
        self.phy=phy
        self.chem=chem
        self.maths=maths
    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.sapid}")
        print(f"Phy: {self.phy}")
        print(f"Chem: {self.chem}")
        print(f"Marks: {self.maths}")
        print(f"Marks percentage:{(self.maths+self.chem+self.phy)/3}%")
        if ( math > 40 and  phy > 40 and chem > 40):
            print("PASS")
        else:
            print("FAIL")
s=[]
n=int(input("Enter the number of students:"))
for i in range(n):
    name=input("Enter name:")
    sap=int(input("Enter sapid:"))
    phy=int(input("Enter physics marks"))
    chem=int(input("Enter chemistry marks"))
    math=int(input("Enter maths marks"))
    std1 = student(name, sap,phy,chem,math)
    s.append(std1)
for i in range(n):
    std1.print_details()