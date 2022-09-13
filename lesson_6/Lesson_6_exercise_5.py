# Exercise 5
from collections import namedtuple
from math import sqrt
# 1.
Point = namedtuple('Point', ['x', 'y'])

# 2.
point_one = Point(x=1, y=1)
point_two = Point(x=8, y=8)

# 3.
board = [["-"]*10 for i in range(10)]

board[point_one.x][point_one.y] = '*'
board[point_two.x][point_two.y] = '*'

for row in board:
    print(row)

# 4.
distance = sqrt((point_one.x - point_two.x)**2 + (point_one.y - point_two.y)**2)
print(f"The distance between {point_one} & {point_two} is {distance}")