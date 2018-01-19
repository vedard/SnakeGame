import math


class Vector():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def normalize(self):
        length = self.length()

        if length != 0:
            self.x /= length
            self.y /= length
            self.z /= length

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def cross(self, vector):
        return Vector(
            self.y * vector.z - self.z * vector.y,
            self.z * vector.x - self.x * vector.z,
            self.x * vector.y - self.y * vector.x,
        )

    def dot(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    def angle(self, vector):
        return math.degrees(
            math.acos(self.dot(vector) / (self.length() * vector.length()))
        )

    def __repr__(self):
        return str((self.x, self.y, self.z))

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, int):
            return Vector(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, int):
            return Vector(self.x - other, self.y - other, self.z - other)

    def __mul__(self, number):
        return Vector(self.x * number, self.y * number, self.z * number)

    def __truediv__(self, number):
        return Vector(self.x / number, self.y / number, self.z / number)

    def __floordiv__(self, number):
        return Vector(self.x // number, self.y // number, self.z // number)

    def __eq__(self, vector):
        return (self.x == vector.x and self.y == vector.y and self.z == vector.z)
