# Exercise 1
# 1:
firstname = "john"
lastname = "smith"
tele = "00468123456789"

print(firstname, lastname, tele)

# 2/3:
fullname = firstname + " " + lastname
print(fullname)

# 4:
print(len(fullname))
print(len(firstname))
print(len(lastname))

# 5:
print(fullname,"\n",tele)

# 6:
print("Firstname: " + firstname, "Lastname: " + lastname, "Tele: " + tele)
print(f'Firstname: {firstname} Lastname: {lastname} Tele: {tele}')
print("Firstname: {} Lastname: {} Tele: {}".format(firstname, lastname, tele))
print("Name %s" %firstname+lastname+tele)

#Exercise 2
# 1:
print(fullname[:6])

# 2:
print(fullname[1:9])

# 3:
print(fullname[::2])

# 4:
print(fullname[::-1])

# 5:
print(fullname[5:6])