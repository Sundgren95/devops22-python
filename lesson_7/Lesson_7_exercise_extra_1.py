# Exercise extra 1
num = int(input("Please enter a number: "))

if num <= 5:
    for n in range(1, int(num)+1):
        number = str(n) * int(n)
        print(number)
if num > 5:
    print(str(num)*num)

def minus_five(num):
    for i in range(1,int(num)+1):
        print(i*str(i))

def plus_five(x):
    print(str(num)*num)

num = int(input("Please enter a number: "))
if num <= 5:
    minus_five(num)
if num > 5:
    plus_five(num)