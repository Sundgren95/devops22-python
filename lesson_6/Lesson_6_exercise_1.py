# Exercise 1
import random

# 1.1
one_to_hundred = [x for x in range(1, 101)]
print(one_to_hundred)

# 1.2
even_numbers = [num for num in range(2,61) if num % 2 == 0]
print(even_numbers)

# 1.3
odd_numbers = [num for num in range(1,78) if num % 2 == 1]
print(odd_numbers)

# 1.4.1
random_list_1 = random.sample(range(1, 300), 100)
print(sorted(random_list_1))

# 1.4.2
random_list_2 = random.choices(range(1, 300), k=100)
print(sorted(random_list_2))

# 1.5
colors = ["blue", "green", "yellow", "purple", "brown"]

# 1.5.1
colors_2 = ["red"]
colors_2.extend(random.sample(colors, k=2))
print(colors_2)

# 1.5.2
colors_3 = random.choices(colors_2, k=50)
print(colors_3)

# 1.5.3
print(f'{len(colors)}, {", ".join(set(colors))}')

print(len(colors_2))
print(set(colors_2))

print(len(colors_3))
print(set(colors_3))