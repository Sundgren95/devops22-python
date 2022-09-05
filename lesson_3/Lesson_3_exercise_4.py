# Övning 4
# 1
my_list = []
# 2
print("red")
# 3
my_list.append("red")
# 4
print(my_list[0])
# 5
my_list.append("blue")
my_list.append("green")
print(my_list)
# 6
print(f'{"red" in my_list}')
# 7
print(f'{"pink" not in my_list}')
# 8
my_list_2 = ["black", "white"]
print(my_list + my_list_2)
# 9
my_list_3 = ["red" , "yellow"]
my_list_3 *= 3
print(my_list_3)
# 10
print(my_list_3[0:4])
# 11
print(my_list_3.count("red"))
# 12
print(my_list_3.index("yellow"))
# 13
print(len(my_list) , len(my_list_2), len(my_list_3))
# 14
my_list_4 = [47, 4, 5, 7, 24, 12, 10]
print(min(my_list_4), max(my_list_4))