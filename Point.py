import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, p):
        if not isinstance(p, Point):
            return False
        return self.x == p.x and self.y == p.y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def distance(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt((dx**2 + dy**2))



