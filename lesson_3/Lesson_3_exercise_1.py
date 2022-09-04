# Uppgift A
x = 1
y = 4
addresses = {"Adam": "Ormvägen 5",
    "Bella": "Klockgatan 1",
    "Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, x, 6}
numbers2 = {y, 2, 3, 4, 7}
# 1: Konstonanter / int
# 2: dict
# 3: 
print(f'{addresses["Bella"]}')
# 4:
addresses["Daniel"] = "Prinsgränd 2"
print(f'{addresses["Daniel"]}')
# 5:
result_1 = len(addresses)
print(f'{list(addresses)}')
print(result_1)
# 5.1:
a = sorted(addresses)[-1]
print(f'{addresses[a]}')
# 5:2
addresses = {v: k for k, v in addresses.items()}
b = sorted(addresses)[0]
print(f'{addresses[b]}')
# 6: list
# 7: x: andra bilen i listan y: 5 bilen i listan
print(f'{cars[x]}')
# 8: y: 5 bilen i listan (nu kan den inte skriva ut något för det inte finns en 5:e bil)
#print(cars[y])
# 9:
cars.sort()
print(f'{cars[0]}')
# 10: Cars2 får sitt innehåll från cars
cars_2 = cars
cars.append("Saab")
print(f'{cars}')
print(cars_2)
# 10.1: 
cars_3 = cars.copy()
cars.append("Tesla")
print(f'{cars_3}')
print(f'{cars}')
# 10.2:
cars = cars*2
print(f'{cars}')
cars.sort()
cars.reverse()
print(f'{cars}')
# 10:3:
unique_cars = cars
unique_cars = list(dict.fromkeys(unique_cars))
print(cars)
print(unique_cars)
# 11: set
# 12: går ej ha dubbletter, skriver därför inte ut x, y
print(numbers1)
print(numbers2)
# 13: 
print(f'Intersection {numbers1 & numbers2}')
# 14:
print(f'union {numbers1 | numbers2}')
# 15: 
print(f'difference {numbers1 - numbers2}')
print(f'difference {numbers2 - numbers1}')