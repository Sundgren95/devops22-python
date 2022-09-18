# Exercise 2 init

class Animal:
    
    def __init__(self, age):
        self.age = age

class Dog:

    def __init__(self, color):
        self.bark = "woff woff"
        self.color = color

class Supermarket:

    def __init__(self, year, close, open):
        self.year = year
        self.close = close
        self.open = open

class Coop:

    def __init__(self, food, clothes, scanning, eshop):
        self.food = food
        self.clothes = clothes
        self.scanning = scanning
        self.eshop = eshop

if __name__ == '__main__':
    myclass = Dog("brown")
    print(myclass.bark)
    print(myclass.color)
    