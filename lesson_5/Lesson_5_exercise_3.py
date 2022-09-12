# Exercise 3:
# 1,2:
price = int(input("Enter the price of your new car: "))
print(f'Your new car costs {price} \U000020AC')

# 3:
if price > 50000:
    print("\U0001F92F")
elif price < 50000:
    print("\U0001F634")