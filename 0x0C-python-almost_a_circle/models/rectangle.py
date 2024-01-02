#!/usr/bin/python3


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new instance of the Rectangle class.

        args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner of the rectangle.
            y (int, optional): The y-coordinate of the top-left corner of the rectangle.
            id (int, optional): The unique identifier.
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y