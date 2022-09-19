# Exercise 2 menu
import sys
class Menu:
    brand = []
    main_menu_text = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'

1: 'Create a car',
2: 'Print the car',
3: 'Delete the car'
4: 'Quit program'
"""
    def __init__(self):
        self.run = False
        self.main_menu_commands = {1: self.create_car, 2: self.print_car,
                                    3: self.delete_car, 4: self.quit}


    def c_car(self):
        brand = []
        brand.append(input("Enter a brand: "))
        self.brand = brand
        return brand

    def create_car(self):
        self.c_car()


    def print_car(self):
        if not self.brand == []:
            print(f'This is your car brand {self.brand}')
        else:
            print("No object available to print")


    def del_car(self):
        if not self.brand == []:
            self.brand.clear()
        else:
            print("No object to delete")

    def delete_car(self):
        self.del_car()


    def quit(self):
        print('Shutting down')
        self.run = False
        sys.exit(0)

    def main_menu(self):
        print(f'{Menu.main_menu_text}')

    def execute_command(self, menu, choice):
        try:
            menu[choice]()
        except Exception as e:
            print(e)
            print('something went wrong')

    def start_loop(self):
        self.run = True
        while self.run:
            self.main_menu()
            choice = int(input('Enter your choice [1-4]: '))
            self.execute_command(self.main_menu_commands, choice)



def main():
    menu = Menu()
    menu.start_loop()
    

if __name__ == '__main__':
    main()