import Equation_modules  # importing a python file containing all the formulas for area & perimeter of all polygons


class Circle:
    '''
    This class is about calculating the area & perimeter using radius
    :return the area & perimeter of the circle
    '''
    def __init__(self, radius):
        self.radius = radius

    def area_circle(self):
        return Equation_modules.circle_area(self.radius)  # Imports the equation to calculate the area of the circle from Equation_modules.py

    def perimeter_circle(self):
        return Equation_modules.circle_perimeter(self.radius)  # Imports the equation to calculate the perimeter of the circle from Equation_modules.py


class Square:
    '''
    This class is about calculating the area & perimeter using length
    :return the area & perimeter of the square
    '''
    def __init__(self, length):
        self.length = length

    def area_square(self):
        return Equation_modules.square_area(self.length)   # Calculating the area using Equation_modules.p

    def perimeter_square(self):
        return Equation_modules.square_perimeter(self.length)   # Calculating the perimeter using Equation_modules.p


class Rectangle:
    '''
    This class is about calculating the area & perimeter using length, width
    :return the area & perimeter of the rectangle
    '''
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_rectangle(self):
        return Equation_modules.rectangle_area(self.length, self.width)  # Calculating the area using Equation_modules.p

    def perimeter_rectangle(self):
        return Equation_modules.rectangle_perimeter(self.length, self.width)  # Calculating the perimeter using Equation_modules.p


class Triangle:
    '''
    This class is about calculating the area & perimeter using base, height, width
    :return the area & perimeter of the triangle
        '''
    def __init__(self, base, height, width):
        self.base = base
        self.height = height
        self.width = width

    def area_triangle(self):
        return Equation_modules.triangle_area(self.base, self.height)  # Calculating the area using Equation_modules.p

    def perimeter_triangle(self):
        return Equation_modules.triangle_perimeter(self.base, self.height, self.width)  # Calculating the perimeter using Equation_modules.p


Square = Square(5)  # sitting the length value
print("area of the square = ", Square.area_square())
print("perimeter of the square = ", Square.perimeter_square())

Circle = Circle(10)  # sitting the radius value
print("area of the circle = ", Circle.area_circle())
print("perimeter of the circle = ", Circle.perimeter_circle())

Triangle = Triangle(5, 6, 2)  # sitting the base, height, and width values
print("area of the triangle = ", Triangle.area_triangle())
print("perimeter of the triangle = ", Triangle.perimeter_triangle())

Rectangle = Rectangle(2, 2)  # sitting the length, and width values
print("area of the rectangle = ", Rectangle.area_rectangle())
print("perimeter of the rectangle = ", Rectangle.perimeter_rectangle())
