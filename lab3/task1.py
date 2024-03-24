from math import sqrt
from uuid import uuid4

class InvalidFigureError:
    pass

class Point:
    def __init__(self, x, y):
        if not all(isinstance(arg, int) or isinstance(arg, float) for arg in (x, y)):
            raise TypeError("Coords should have int or float type")
        self.x = x
        self.y = y
        self.id = uuid4()

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getId(self):
        return self.id

    def setX(self, value):
        self.x = value
    
    def setY(self, value):
        self.y = value

    def getCoords(self):
        return self.x, self.y
    
    def dist(self, p):
        return sqrt((self.x - p.getX()) ** 2 + (self.y - p.getY()) ** 2)

class Triangle:
    def __init__(self, p1, p2, p3):
        if not all(isinstance(arg, Point) for arg in (p1, p2, p3)):
            raise TypeError("Points should have Point type")
        p = (p1.dist(p2) + p2.dist(p3) + p3.dist(p1)) / 2 
        if not p * (p - p1.dist(p2)) * (p - p2.dist(p3)) * (p - p3.dist(p1)):
            raise InvalidFigureError("Invalid triangle")
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.id = uuid4()

    def getP1(self):
        return self.p1
    
    def getP2(self):
        return self.p2

    def getP3(self):
        return self.p3
    
    def getId(self):
        return self.id

    def setp1(self, value):
        self.p1 = value
    
    def setp2(self, value):
        self.p2 = value

    def setp3(self, value):
        self.p3 = value

    def getPoints(self):
        return self.p1, self.p2, self.p3

    # двумерный вектор 'v' прикладывается к каждой точке, и на него производится смещение
    def move(self, v):
        if not isinstance(v, list) and not isinstance(v, tuple):
            raise TypeError("Vector v should have tuple or list type")
        for point in (self.p1, self.p2, self.p3):
            point.setX(point.getX() + v[0])
            point.setY(point.getY() + v[1])

class Pentagon(Triangle):
    def __init__(self, p1, p2, p3, p4, p5):
        if not all(isinstance(arg, Point) for arg in (p1, p2, p3, p4, p5)):
            raise TypeError("Points should have Point type")
        # Pentagon center
        cx = sum([point.getX() / 5 for point in (p1, p2, p3, p4, p5)])
        cy = sum([point.getY() / 5 for point in (p1, p2, p3, p4, p5)])
        c = Point(cx, cy)
        if not p1.dist(c) == p2.dist(c) == p3.dist(c) == p4.dist(c):
            raise InvalidFigureError("Invalid tetragon") 
        super().__init__(p1, p2, p3)
        self.p4 = p4
        self.p5 = p5
        # id есть за счет Triangle

    def getP4(self):
        return self.p4

    def setp4(self, value):
        self.p4 = value

    def getP5(self):
        return self.p5

    def setp5(self, value):
        self.p5 = value

    def getPoints(self):
        # added comma to create tuple
        return super().getPoints() + (self.p4,) + (self.p5)

    # двумерный вектор 'v' прикладывается к каждой точке, и на него производится смещение
    def move(self, v):
        if not isinstance(v, list) and not isinstance(v, tuple):
            raise TypeError("Vector v should have tuple or list type")
        super().move(v)
        self.p4.setX(self.p4.getX() + v[0])
        self.p4.setY(self.p4.getY() + v[1])
        self.p4.setX(self.p5.getX() + v[0])
        self.p4.setY(self.p5.getY() + v[1])