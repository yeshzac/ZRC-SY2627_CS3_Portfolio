class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

@property
def width(self):
    return f"{self.__width:.1f}cm"

@property
def height(self):
    return f"{self.__height:.1f}cm"

@width.setter
def width(self, new_width):
    if new_width > 0:
        self.__width = new_width
    else:
        print("width must be greater than zero")

@height.setter
def height(self, new_height):
    if new_height > 0:
        self.__height = new_height
    else:
        print("height must be greater than zero")

@width.deleter
def width(self):
    del self.__width
    print("width has been deleted")

@height.deleter
def height(self):
    del self.__height
    print("height has been deleted")