#!/usr/bin/python3
"""Represents a rectangle."""


class Rectangle:
    """Represents the rectangle"""

    number_of_instances = 0
    """Number of active instances"""

    print_symbol = "#"
    """Symbol for string representation"""

    def __init__(self, width=0, height=0):
        """Initialization for rectangle
            Args:
                width (int): The width of the rectangle
                height (int): The height of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter/setter for width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter/setter for the height if the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Represents and returns the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Represents and returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = []
        for j in range(self.__height):
            for i in range(self.__width):
                rectangle_str.append(str(self.print_symbol))
            if j != self.__height - 1:
                rectangle_str.append("\n")
        return ("".join(rectangle_str))

    def __repr__(self):
        rectangle_str = "Rectangle(" + str(self.__width)
        rectangle_str += ", " + str(self.__height) + ")"
        return (rectangle_str)

    def __del__(self):
        """Prints a message after every deletion of a string"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
