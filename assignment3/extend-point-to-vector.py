#Task 5 

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)

# this will inherits from Point
class Vector(Point):
    def __str__(self):
        return f"Vector[{self.x}, {self.y}]"

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

# Demonstration
if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    p3 = Point(0, 0)

    print(p1)  
    print(p1 == p2)  
    print(p1.distance_to(p3))  # 5.0

    v1 = Vector(1, 2)
    v2 = Vector(4, 6)
    print(v1) 

    v3 = v1 + v2
    print(v3)  
