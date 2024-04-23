import random

CompNumber = random.randrange(1, 101)
userInput = int(input("Enter Your Number:--"))

if userInput > CompNumber:
    print("Computer Number", CompNumber)
    print("Your guess is high")
elif CompNumber > userInput:
    print("Computer Number", CompNumber)
    print("Your guess is low")
else:
    print("Computer Number", CompNumber)
    print("Your guess is equal")
