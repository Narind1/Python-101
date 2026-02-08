class Shape:
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 2 * (self.width + self.height)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
class Square(Shape):
    def __init__(self,side):
        self.side=side
rectangle = Rectangle(5,4)
square= Square(3)
print("Rectangle perimeter:", rectangle.perimeter())
print("Area of square",square.area())