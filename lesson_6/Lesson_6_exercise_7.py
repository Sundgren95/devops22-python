# Exercise 7
from copy import copy, deepcopy
# 1.
names = ["Adam", "Bertil", "Caesar", "David", "Erik"]

# 2.
x = names

# 3.
names_copy = copy(names)
names_deep_copy = deepcopy(names)

# 4.
names.pop()
names.append("Elin")

# 5.
print(names)
print(x)
print(names_copy)
print(names_deep_copy)