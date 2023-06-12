import random
randomnumber=random.randint(1,100)
#print(randomnumber)
userguess=None
guesses=0

while userguess!=randomnumber:
    userguess=int(input("Enter the number :"))
    guesses+=1
    if userguess==randomnumber:
        print("You guessed right!!")
    else:
        if randomnumber<userguess:
            print("You gussed it wrong! Enter a smaller number")
        else:
            print("You guseed it wrong! Enter a larger number")

print(f"Ypu gussed this number in {guesses} guesses")
with open("highscore.txt","r")as f:
    highscore=int(f.read())

if highscore>guesses:
    print("You just break a highscore")
    with open("highscore.txt","w")as f:
        f.write(str(guesses))