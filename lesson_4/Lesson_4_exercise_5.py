# Exercise 5

while True:
    print("Enter stop to quit:")
    stop = input()
    if stop == "stop" :
        break
    else:
        print(f'You wrote: {stop} and the length is: {len(stop)}')   