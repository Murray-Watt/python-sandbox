# The purpose of this code is to demonstrate how to implement
# an operator
#
# The Vector class implements the following operators:
# __repr__ - returns a string representation of the object
# __abs__ - returns the magnitude of the vector
# __bool__ - returns True if the vector is not zero (i.e. it has a magnitude)
# __add__ - returns the sum of two vectors
# __mul__ - returns the product of a vector and a scalar
#
# The bool() function returns the boolean value of a specified object.
#
# The object will always return True, unless:
#
# The object is empty, like [], (), {}
# The object is False
# The object is 0
# The object is None
#
import math


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
