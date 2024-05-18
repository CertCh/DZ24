import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def is_on_axis(self):
        return self.x == 0 or self.y == 0


point1 = Point(0, 0)
point2 = Point(3, 4)
print(point1.distance_to(point2))  
point1.move(1, 1)
print(point1.is_on_axis())  
