# Exercise 1 override

class Car:
    def open_hood(self):
        return print("Open the hood, showing nice engine")


class Telsa(Car):
    def open_hood(self):
        return print("Open the hood, no engine found")


def main():
    open = Car()
    print(open.open_hood())
    open_2 = Telsa()
    print(open_2.open_hood())


if __name__ == '__main__':
    main()