class grandma:
    def __init__(self,age):
        self.age=age
        print(f"Hello Im Grandma Im {self.age} years old")
class parent(grandma):
    def __init__(self,gender):
        #self.age=age
        self.gender=gender
        print(f"Hello Im parent Im years old and {self.gender} ")
class son(parent):
    def __init__(self,age,gender,name):
        self.age=age
        self.gender=gender
        self.name=name
        print(f"Hello Im {self.name} Im {self.age} years old {self.gender}.")
a=grandma(99)
b=parent("Male")
c=son(40,"Male","Ash")