import math


def circle_area(radius):
    return radius ** 2 * math.pi


def circle_perimeter(radius):
    return 2 * radius * math.pi


def triangle_area(base, height):
    return 0.5 * base * height


def triangle_perimeter(base, height, width):
    return base + height + width


def square_area(length):
    return length ** 2


def square_perimeter(length):
    return 4 * length


def rectangle_area(length, width):
    return length * width


def rectangle_perimeter(length, width):
    return 2*(length * width)
