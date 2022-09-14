# Exercise 1 Functions
# 1.
def do_nothing():
    pass
do_nothing()

# 2.1
def hello():
    print("Hello World")
hello()

# 2.2
def num():
    print(1 == 1.0)
num()

# 2.3
import string
def alpha():
    print(string.ascii_lowercase[::-1])
alpha()

# 3.1
def greet_name(name, hello="Hello"):
    print(f'{hello} {name}')
greet_name("Kalle")

# 3.2
def capital(word):
    print(f'{word.upper()}')
capital("hello world")

# 3.3
def one_stop(stop):
    for number in range(1, stop):
        print(number)
one_stop(10)