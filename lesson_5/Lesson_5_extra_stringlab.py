# Exercise 1

first_string = input("Enter a string: ")
second_string = input("Enter a second string: ")

new_first_string = "'" + first_string + "'"
new_second_string = '"' + second_string + '"'

string = (new_first_string + "\n" + new_second_string)

print(string)
print(f'{new_first_string}\n{new_second_string}')

# Exercise 2



# Exercise 3

start = "Jag tYcker om äGg"
goal = "jAG tYCKER iNTE oM SPAM"

words = start.split()
words[0] = words[0].swapcase()
words[1] = words[1].capitalize().swapcase()
words.insert(2, "inte".capitalize().swapcase())
words[3] = words[3].capitalize().swapcase()
words[4] = "SPAM"

print(words)
print(" ".join(words))