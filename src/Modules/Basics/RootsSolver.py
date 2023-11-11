# This is a simple program that solves quadratic equations.
# It is used to demonstrate how to create unittests
import math

def roots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        disc = math.sqrt(d)
        root1 = (-b + disc) / (2 * a)
        root2 = (-b - disc) / (2 * a)
        return root1, root2
    elif d == 0:
        return -b / (2 * a)
    else:
        return "This equation has real roots"


class RootsSolver:
    pass


if __name__ == '__main__':
    solver = RootsSolver()
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    result = roots(a, b, c)
    print(result)