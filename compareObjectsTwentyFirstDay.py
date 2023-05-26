class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def __gt__(self,other):
        return self.x > other.x and self.y > other.y

point = Point(1, 2)
another = Point(1, 2)
print(point == another)

pointGt = Point(3, 5)
anotherGt = Point(1, 2)
print(pointGt > anotherGt)