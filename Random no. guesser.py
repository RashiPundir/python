# This is a sample Python script.
import random
print("Hey! This is a Rock-Paper-Scissors Game between you and CPU")
print("Enter your name")
name = input()
q = {"s","p","sc"}
i = random.choice(q)
p=0
antip=0
while p<=5 or antip<5:
    print("Play")
    move = input()
    if i == 's':
        if move == 's':
            print("Cpu : Stone ")
            print("You : Stone ")
            print("No points play again")
            print("You:", p, "CPU:", antip)
        if move == 'p':
            print("Cpu : Stone ")
            print("You : Paper ")
            print("CPU wins this point")
            antip += 1
            print("You:", p, "CPU:", antip)
        if move == 'sc':
            print("Cpu : Stone ")
            print("You : Scissors ")
            print("This point goes to you")
            p += 1
            print("You:",p,"CPU:",antip)
    if i == 'p':
        if move == 's':
            print("Cpu : Paper ")
            print("You : Stone ")
            print("CPU wins this point")
            antip += 1
            print("You:", p, "CPU:", antip)
        if move == 'p':
            print("Cpu : Peper ")
            print("You : Paper ")
            print("No points play again")
            print("You:", p, "CPU:", antip)
        if move == 'sc':
            print("Cpu : Paper ")
            print("You : Scissors ")
            print("This point goes to you")
            p += 1
            print("You:",p,"CPU:",antip)
    if i == 'sc':
        if move == 's':
            print("Cpu : Scissors ")
            print("You : Stone ")
            print("This point goes to you")
            p += 1
            print("You:", p, "CPU:", antip)
        if move == 'p':
            print("Cpu : Scissors ")
            print("You : Paper ")
            print("CPU wins this point")
            antip += 1
            print("You:", p, "CPU:", antip)
        if move == 'sc':
            print("Cpu : Scissors ")
            print("You : Scissors ")
            print("No points play again")
            print("You:", p, "CPU:", antip)
if p == 5:
    print(name,"won the match")
else:
    print("CPU won the match")
end =input("Now press 1 to exit")

