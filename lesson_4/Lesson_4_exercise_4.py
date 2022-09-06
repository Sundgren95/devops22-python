# Exercise 4

start = int(input("Enter a start number: "))
stop = int(input("Enter a stop number: "))

for i in range(start, stop):
    print(i)

total = sum(range(start, stop))

print(total)
