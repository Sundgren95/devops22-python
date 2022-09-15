# Exercise 3 try/except

def try_except(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    except TypeError:
        print("String is not allowed")

# Alt
def div(x, y):
   not_a_string(y)
   try:
      return x/y
   except ZeroDivisionError:
      print('Division by zero is not allowed')


def not_a_string(y):
   if isinstance(y, str):
      raise TypeError("String is not allowed")


div(1, 1)
# div(1, 0)
# div(1, "1")