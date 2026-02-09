class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __sub__(self,other):
        return Point(self.x - other.x, self.y - other.y)
    def __repr__(self):
        return f"P({self.x},{self.y})"
P1 = Point(30, 20)
P2 = Point(25, 15)
P3 = P1 - P2
print(P1)
print(P2)
print(P3)