import math


def getArea(r, pi=math.pi):
    """Doiraning yuzasini qaytaruvchi funksiya"""
    return pi * (r ** 2)


def getPerimeter(r, pi=math.pi):
    """Doiraning perimetrini qaytaruvchi funksiya"""
    return 2 * pi * r


print(getArea(5))
print(getPerimeter(5))
