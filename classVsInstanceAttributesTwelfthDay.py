class Point:
    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x},{self.y})")


point = Point(1, 3)
print(point.default_color)
print(Point.default_color)
point.z = 10
print(point.z)

Point.default_color = "blue"
print(point.default_color)
print(Point.default_color)
