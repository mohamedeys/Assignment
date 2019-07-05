import Equation_modules  # importing a python file containing all the formulas for area & perimeter of all polygons


class Polygons:
    '''
    This is the master class and it determines the shape of the polygon for further calculations
    :return "circle" or "square" "triangle" or "rectangle"
    '''
    def __init__(self, shapes):
        self.shapes = shapes

    def show_shape(self):
        self.shapes = input("Enter the shape required for further calculations: ")


class Circle(Polygons):
    '''
    This class is about calculating the area & perimeter using radius
    :return area of the circle =  & perimeter of the circle =
    '''
    def __init__(self, radius):
        Polygons.__init__(self, 'circle')
        self.radius = radius

    def area(self):
        return Equation_modules.circle_area(self.radius)  # Imports the equation to calculate the area of the circle from Equation_modules.py

    def perimeter(self):
        return Equation_modules.circle_perimeter(self.radius)  # Imports the equation to calculate the perimeter of the circle from Equation_modules.py


class Square(Polygons):
    '''
    This class is about calculating the area & perimeter using length
    :return area of the square =  & perimeter of the square =
    '''
    def __init__(self, length):
        Polygons.__init__(self, 'square')
        self.length = length

    def area(self):
        return Equation_modules.square_area(self.length)   # Calculating the area using Equation_modules.p

    def perimeter(self):
        return Equation_modules.square_perimeter(self.length)   # Calculating the perimeter using Equation_modules.p


class Rectangle(Polygons):
    '''
    This class is about calculating the area & perimeter using length, width
    :return area of the rectangle =  & perimeter of the rectangle =
    '''
    def __init__(self, length, width):
        Polygons.__init__(self, 'rectangle')
        self.length = length
        self.width = width

    def area(self):
        return Equation_modules.rectangle_area(self.length, self.width)  # Calculating the area using Equation_modules.p

    def perimeter(self):
        return Equation_modules.rectangle_perimeter(self.length, self.width)  # Calculating the perimeter using Equation_modules.p


class Triangle(Polygons):
    '''
    This class is about calculating the area & perimeter using base, height, width
    :return area of the triangle =  & perimeter of the triangle =
        '''
    def __init__(self, base, height, width):
        Polygons.__init__(self, 'triangle')
        self.base = base
        self.height = height
        self.width = width

    def area(self):
        return Equation_modules.triangle_area(self.base, self.height)  # Calculating the area using Equation_modules.p

    def perimeter(self):
        return Equation_modules.triangle_perimeter(self.base, self.height, self.width)  # Calculating the perimeter using Equation_modules.p


polygon_triangle = Triangle(5, 5, 5)
print("The shape entered is: {}".format(polygon_triangle.show_shape()))
print('area of the triangle = ', polygon_triangle.area())
print('perimeter of the triangle = ', polygon_triangle.perimeter())
'''
polygon_square = Square(5)
print(polygon_square.show_shape())
print("Area of the square = ", polygon_square.area())
print("Perimeter of the square = ", polygon_square.perimeter())

'''
'''
polygon_triangle = Triangle(5, 5, 5)
print("Type of Polygon => ", Polygons.show_shape)
print("Area = ", polygon_triangle.area)
print("Perimeter = ", polygon_triangle.perimeter)

polygon_square = Square(5)
print("Type of Polygon => ", Polygons.show_shape)
print("Area = ", polygon_square.area)
print("Perimeter = ", polygon_square.perimeter)

polygon_circle = Circle(5)
print("Type of Polygon => ", Polygons.show_shape)
print("Area = ", polygon_circle.area)
print("Perimeter = ", polygon_circle.perimeter)

polygon_rectangle = Rectangle(5, 5)
print("Type of Polygon => ", Polygons.show_shape)
print("Area = ", polygon_rectangle.area)
print("Perimeter = ", polygon_rectangle.perimeter)
'''



'''
tri = Triangle(2, 2, 2)
rect = Rectangle(2, 3)
circle = Circle(3)
square = Square(5)

figures = [tri, rect, circle, square]
for fig in figures:
    print ("Type of Polygon =>", fig.show_shape())
    print ("Area =", fig.area())
    print ("Perimeter =", fig.perimeter())
'''

'''
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
'''