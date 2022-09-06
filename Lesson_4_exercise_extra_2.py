# Exercise extra
# 4:
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 19, 20]

for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        print("Not allowed")
        break

# 5: 
first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]
output = []

for i in second_list:
    output.append((i, first_list.index(i)))
print(output)

# 7:
fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
basket = []
x = len(fruits)
space = int(input("How much space do you have in your basket? "))
for i in range(space):
    basket.append(fruits[i%x])
print(basket)

# 8:
num = 1
while(num <= 100):
    count = 0
    i = 2
    while(i <= num//2):
        if(num % i == 0):
            count = count + 1
            break
        i = i + 1
    if (count == 0 and num!= 1):
        print(num, end = " ")
    num = num + 1