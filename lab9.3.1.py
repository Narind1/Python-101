class area:
    def area(self):
        return self.width*self.height
class peri:
    def perimeter(self):
        return 2*self.width*self.height
class rectangle(area,peri):
    def __init__(self,width,height):
        self.width=width
        self.height=height
rect=rectangle(2,3)
print("Area:",rect.area())
print("Perimeter",rect.perimeter())