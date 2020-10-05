# This is a sample Python script.
import random
print("Hey! The random no. is between 1 to 10")
print("You have 4 chances to guess the no.")
i = random.randint(1,10)
trys=0
while trys<5:
    print("Now try guessing")
    nos = int(input())
    trys += 1
    if nos > i:
        print("You guessed too high")
    if nos < i:
        print("You guessed too low")
    if nos == i:
        break
if nos == i:
    print("You guessed the no. right. The no. was:",nos)
    print("You took",trys,"trys")
if nos != i:
    print("You Loose the no. was:",nos)

