# Exercise 2

names = ("lars", "mikael", "anders", "johan", "erik")

name = input("Enter your name to see if you are on the list: ").lower()

if name in names:
    print(f'Welcome {name.capitalize()} you are on the list')
else:
    print(f'Sorry, you are not on the list')