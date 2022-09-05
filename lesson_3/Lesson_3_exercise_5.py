# Övning 5
cars = ["volvo", "audi", "bmw", "tesla", "ferrari", "skoda", "volkswagen", "kia", "honda", "toyota"]
# 1
print(sorted(cars))
# 2
cars.sort()
print(cars)
# 3
print(sorted(cars, reverse=True))
cars.sort(reverse=True)
print(cars)
# 4
cars_2 = [("volvo", "v90"),("audi", "a4"),("bmw", "320"),("tesla", "model y"),("ferrari", "f40"),
("skoda", "enyaq"),("volkswagen", "tiguan"),("kia", "ceed"),("honda", "civic"), ("toyota", "supra")]
cars_2.sort()
print(cars_2)
print(sorted(cars_2, key=lambda x:x[1]))