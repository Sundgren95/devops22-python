# Exercise extra
#1:
for i in range(10):
    print("Hello user")

# 2:
n = 9
for i in range(1,n+1):
    for j in range(1, i+1):
        print(i, end="")
    print()

# 3:
while True:
    number = int(input("Enter a number: "))
    if(number == 55):
        print("Congratulations, that's the right number")
        break
    elif(number < 55):
        print("Wrong, the number is higher!")
    elif(number > 55):
        print("Wrong, the number is lower!")