# Exercise 4
from collections import deque
import random
# 1.
names = ["Lisa", "Pelle", "Olle", "Bertil", "Caesar", "David"]
counted_names = random.choices(names, k=50)

# 2.
queue = [counted_names.pop() for i in range(10)]
queue = deque(queue)

# 3-5.
while len(queue) > 0:
    print(queue)
    leave_queue = random.choice(range(1,len(queue) + 1))
    for i in range(leave_queue):
        queue.popleft()
    for i in range(leave_queue):
        if len(counted_names) < 1:
            break
        queue.append(counted_names.pop())
print(queue)