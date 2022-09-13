# Exercise 3
import string
# 1.
abc = list(string.ascii_lowercase)
print(abc)

# 2.
stack = []
for i in abc:
    stack.append(1)
print(stack)

# 3.
my_string = ""
while stack:
    my_string += stack.pop()
print (my_string)


"""for i in range(len(stack)):
    print(stack.pop(), end=" ")
print(stack)"""