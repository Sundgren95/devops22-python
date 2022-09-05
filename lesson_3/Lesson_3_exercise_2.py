# Uppfift B
# A list that holds the name, age and shoe size of the 3 people
people = [{
    "name" : input("Enter name for person 1:\n"),
    "age" : input("Enter age for person 1:\n"),
    "shoe" : input("Enter shoe size for person 1:\n")},
    {
    "name" : input("Enter name for person 2:\n"),
    "age" : input("Enter age for person 2:\n"),
    "shoe" : input("Enter shoe size for person 2:\n")},
    {
    "name" : input("Enter name for person 3:\n"),
    "age" : input("Enter age for person 3:\n"),
    "shoe" : input("Enter shoe size for person 3:\n")
}]

# Finds the oldest person
age = sorted(people, key=lambda x : x["age"])[-1]
# Finds the person with median shoe size
size = sorted(people, key=lambda x : x["shoe"])[1]

# Prints info of the people
print(f'The oldest person is {age["name"].capitalize()} with shoe size {age["shoe"]}')
print(f'The person with median shoe size is {size["name"].capitalize()} and is {size["age"]} years old')

# Two variables that holds the entered info
value, prop = input('Please enter search value, name, age or shoe followed by value: ').split()

# Variable that sorts the list of persons
search = sorted(people, key=lambda x : x[value] == prop)[-1]

# Prints the info of the requested person
print(f'Name: {search["name"].capitalize()}\nAge: {search["age"]}\nSize: {search["shoe"]}')