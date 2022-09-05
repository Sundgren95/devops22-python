# Övning 3
# 1.1
x = True
y = False
z = True
result = x or y or z
print(result)
print(x>y<z)
# 1.2
x = True
y = True
z = True
result = x or y or z
print(result)
print(x == y == z)
# 1.3
x = True
y = False
z = True
result = x and y and z
print(result)
print(x < y > z)
print(x == y == z)
# 1.4
x = False
y = False
z = False
result = x or y or z
print(result)
print(x > y > z)
# 1.5
x = False
y = True
z = False
result = x and y or z
print(result)
print(x == y == z)
print(x > y < z)
# 1.6
x = True
y = True
z = True
result = not x and y and z
print(result)
print(x != y != z)