from math import sqrt
from uuid import uuid4

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
            raise TypeError("Invalid triangle")
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
        # Pentagon type
        ps = [p1, p2, p3, p4, p5]
        for i in range(len(ps)-2):
            ps.remove(ps[i])
            for j in range(i+1, len(ps)-1):
                ps.remove(ps[j])
                for k in range(j+1,len(ps)):
                    if (ps[k].getY() - ps[j].getY())*(ps[i].getX() - ps[j].getX()) == (ps[k].getX() - ps[j].getX())*(ps[i].getY() - ps[j].getY()):
                        raise TypeError("Invalid pentagon")
                print(j)
                ps.insert(j,ps[j])
            ps.insert(i,ps[i])

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
        return super().getPoints() + (self.p4,) + (self.p5,)

    # двумерный вектор 'v' прикладывается к каждой точке, и на него производится смещение
    def move(self, v):
        if not isinstance(v, list) and not isinstance(v, tuple):
            raise TypeError("Vector v should have tuple or list type")
        super().move(v)
        self.p4.setX(self.p4.getX() + v[0])
        self.p4.setY(self.p4.getY() + v[1])
        self.p5.setX(self.p5.getX() + v[0])
        self.p5.setY(self.p5.getY() + v[1])

# Check if tetragon is valid
try:
    penta = Pentagon(Point(0,1),Point(0,2),Point(0,3),Point(0,4),Point(0,5))
except TypeError as e:
    print(e)

# Check if point is valid
try:
    p = Point("1", "2")
except TypeError as e:
    print(e)

# Check if triangle is valid
try:
    tr = Triangle(Point(0,1),Point(0,2),Point(0,3))
except TypeError as e:
    print(e)

tr = Triangle(Point(0,3),Point(0,0),Point(4,0))
penta = Pentagon(Point(-1,4),Point(0,0),Point(4,0),Point(5,4),Point(2,6))

def is_intersect(pn, tr):
    if not isinstance(tr, Triangle) or not isinstance(pn, Pentagon):
        raise print("Triangle and pentagon types should be passed")
    for i in range(3):
        for j in range(i + 1, 3):
            tr_p1 = tr.getPoints()[i]
            tr_p2 = tr.getPoints()[j]
            # Ax + By + C = 0 - уравнение прямой через точки треугольника
            A1 = (tr_p2.getY() - tr_p1.getY())
            B1 = (tr_p1.getX() - tr_p2.getX())
            C1 = tr_p1.getY()*(tr_p2.getX() - tr_p1.getX()) - tr_p1.getX()*(tr_p2.getY() - tr_p1.getY())
            for m in range(5):
                for n in range(m + 1, 5):
                    pnP1 = pn.getPoints()[m]
                    pnP2 = pn.getPoints()[n]
                    A2 = (pnP2.getY() - pnP1.getY())
                    B2 = (pnP1.getX() - pnP2.getX())
                    C2 = pnP1.getY()*(pnP2.getX() - pnP1.getX()) - pnP1.getX()*(pnP2.getY() - pnP1.getY())
                    # если прямые параллельны, пересечений нет
                    if (A1 * B2 - A2 * B1) == 0:
                        continue
                    # ищем координаты точки пересечения
                    x = -(C1 * B2 - C2 * B1) / (A1 * B2 - A2 * B1)
                    y = -(A1 * C2 - A2 * C1) / (A1 * B2 - A2 * B1)
                    # если координаты точки пересечения лежат на отрезках
                    if x >= max(min(tr_p1.getX(),tr_p2.getX()),min(pnP1.getX(),pnP2.getX())) and x <= min(max(tr_p1.getX(),tr_p2.getX()),max(pnP1.getX(),pnP2.getX())):
                        if y >= max(min(tr_p1.getY(),tr_p2.getY()),min(pnP1.getY(),pnP2.getY())) and y <= min(max(tr_p1.getY(),tr_p2.getY()),max(pnP1.getY(),pnP2.getY())):
                            return True         
    return False

print(is_intersect(penta, tr))
penta.move([9,9])
print(is_intersect(penta, tr))