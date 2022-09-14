# Exercise 3 Return
# 1.
def integer(x):
    return x

x = integer(5)
print(x)

# 2.
def tup(x, y):
    return (x, y)

cords = tup(2, 3)
print(cords)

# 3.
def bool(a, b):
    return a == b

value_1 = bool(2, 2)
value_2 = bool(3, 7)
print(f'{value_1} {value_2}')

# 4.
def float_value(x ,y):
    result = x + y
    return float(result)

float_addition = float_value(1, 4)
print(float_addition)

# 5.
def name(firstname, lastname):
    return firstname + " " + lastname

print(name("mona", "lisa"))

# 6.
def area_rectangle(l, b):
    return l * b

print(area_rectangle(2, 4))

# 7.
def my_function(i):
    sum = 0
    for num in i:
        sum += num
    return sum

numbers = [1, 2, 3, 4]
print(my_function(numbers))

# 8.
def repeat(word, repeat):
    x = word * repeat
    return x
print(repeat("hello ", 3))