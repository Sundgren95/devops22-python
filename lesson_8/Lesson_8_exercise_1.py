# Exercise 1 raise
def check_float(x):
    if type(x) != float:
        raise TypeError("Thats not a float")
    else:
        print("Thats a float")

# Alt
def is_float(value):
   if not isinstance(value, float):
      raise TypeError("Value is not a float")

my_var = 0
is_float(my_var)