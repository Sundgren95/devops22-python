# Exercise 4 circle
from math import pi

class Circle:

    def __init__(self, diagonal):
        self.diagonal = diagonal
        self.area = self.circle_area()
        self.circumference = self.circle_circumference()
        self.color = "grey"

    def circle_area(self):
        radius = self.diagonal / 2
        area = pi * radius ** 2
        return area

    def circle_circumference(self):
        circumference = pi * self.diagonal
        return circumference

    def set_color(self, color):
        self.color = color
        

if __name__ == '__main__':
    myclass = Circle(3)

    print(myclass.area)
    print(myclass.circumference)
    myclass.set_color("red")
    print(myclass.color)