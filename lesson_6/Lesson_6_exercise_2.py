# Exercise 2
from collections import Counter
import random

# 2.1
names = ["Adam", "Bertil", "Caesar", "David", "Erik",
         "Filip", "Gustav", "Helge", "Ivar", "Johan"]
counted_names = random.choices(names, k=100)

# 2.2
c = Counter(counted_names)
print(c)

# 2.3
print(f'Print top 3 names\n{c.most_common(3)}')

# 2.4
print(f'Print the least popular names\n{c.most_common()[-3:]}')

# 2.5
unique = list(set(names))
print(unique)

# 2.5.1
print(sorted(names))

# 2.5.2
random.shuffle(names)
print(names)

# 2.5.3
print(sorted(names, reverse=True))