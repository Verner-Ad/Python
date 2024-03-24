from uuid import uuid4

class Triangle:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.id = uuid4()

    