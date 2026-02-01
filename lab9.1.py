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
s=[]
for i in range(3):
    name=input("Enter name:")
    sap=int(input("Enter sapid:"))
    phy=int(input("Enter physics marks"))
    chem=int(input("Enter chemistry marks"))
    math=int(input("Enter maths marks"))
    std1 = student(name, sap,phy,chem,math)
    s.append(std1)
for i in range(3):
    std1.print_details()
