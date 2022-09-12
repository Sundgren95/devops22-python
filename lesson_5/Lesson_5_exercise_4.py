# Exercise 4

salary = 4000

print(f'Hello employee, your current salary is {salary} \U000020A4')

option_1 = "I want a salary raise"
option_2 = "I want to quit"
first_attempt = 1

while True:
    option = int(input(f'What can I help you with today?\n1. {option_1}\n2. {option_2}\nOption: '))
    attempts = 4

    if option == 1:
        while attempts != 0:
            new_salary = int(input(f'Tell me what salary raise you want: '))
            percent = new_salary / salary * 100
            
            if percent > 10.0 or first_attempt == 1:
                print(f"That's an incresse of {percent}% \U0001F602 and that will be a NO, you can suggest a lower offer!")
                attempts -= 1
                first_attempt = 0

                if attempts == 0:
                    print(f"I'm sorry we cound't find a solution! Come back another time.")
            else:
                print(f'That is an increese of {percent}%, that we can agree on \U0001F91D')
                exit()
    
    elif option == 2:
        print("That's a shame you want to quit. Good luck in the future!")
        break