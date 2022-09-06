# Exercise julius caesar encryption

shifts = int(input("Enter how many shitfs do you want in your message: "))
msg = input("Enter the message you want to encrypt: ").lower()
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in msg:
    if i not in alpha:
        print(i, end="")
        continue
    shiftalpha = (alpha.index(i) + shifts)
    print(alpha[shiftalpha], end="")