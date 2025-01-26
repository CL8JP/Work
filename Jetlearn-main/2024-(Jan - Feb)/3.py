from types import UnionType
from typing import Any


class Point:
    def __init__(self, X = 0, Y = 0):
        self.X = X
        self.Y = Y

    def __str__(self):
        return "({0},{1})".format(self.X, self.Y)
    
    def __add__(self, Other):
        x = self.X + Other.X

        y = self.Y + Other.Y

        return Point(x, y)
    
V1 = Point(1, 2)
V2 = Point(2, 3)
print(V1 + V2)