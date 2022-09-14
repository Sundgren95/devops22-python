# Exercise 2 Default Arguments
# 1.
def one_ten(start=1, stop=11):
    for i in range(start, stop):
        print(i)
one_ten()

# 2/3.
def new_string(string,reverse = False):
    if reverse == True:
        print(string[::-1])
    else:
        print(string)

new_string("hello")
new_string("hello",True)