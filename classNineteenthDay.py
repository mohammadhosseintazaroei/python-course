class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print(f"Point({self.x},{self.y})")


point = Point(1, 3)
point.draw()
print(type(point))
print(point.x)

print(isinstance(point, int))

anouther = Point(4,5)
anouther.draw()

