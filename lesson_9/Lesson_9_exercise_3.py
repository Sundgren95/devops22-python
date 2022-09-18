# Exercise 3 methods

class Square:

    def __init__(self, side):
        self.side = side
    
    def square_area(self):
        area = self.side ** 2
        return float(area)

    def circumference(self):
        circum = self.side * 4
        return float(circum)

if __name__ == '__main__':
    my_object = Square(2)
    print(my_object.square_area())
    print(my_object.circumference())

    my_object_2 = Square(3.5)
    print(my_object_2.square_area())
    print(my_object_2.circumference())