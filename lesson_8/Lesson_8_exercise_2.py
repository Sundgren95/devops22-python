# Exercise 2 input validation 
while True:
    try:
        integer = int(input("Enter a integer: "))       
    except ValueError:
        print("Sorry, not a int")
    else:
        if integer % 2 == False:
            print("Even number is not allowed")
        if integer % 2 == True:
            print(integer)
            break

# alt
def int_input():
   try:
      return int(input("Write a integer: "))
   except:
      print("Sorry, not an int")
      return int_input()

def even_input():
   number = int_input()
   if not number % 2:
      raise Exception('Even numbers is not allowed')
   return number

even_input()