# This is a sample Python script.
import random
print("Hey! Welcome to the Rock-Paper-Scissors Game between you and CPU")
print("Enter your name")
name = input()
print("Rules : s for Stone || p for Paper || sc for Scissors")
q = ("stone","paper","scissors")
p=0
antip=0
while p<=3 and antip<=3:
    print("Play")
    print("Your move ?")
    move = input()
    i = random.choice(q)
    if i == 'stone':
        if move == 'stone':
            print("Cpu : Stone ")
            print("You : Stone ")
            print("No points play again")
            print("You:", p, "CPU:", antip)
        if move == 'paper':
            print("Cpu : Stone ")
            print("You : Paper ")
            print("CPU wins this point")
            print("This point goes to you")
            p += 1
            print("You:", p, "CPU:", antip)
        if move == 'scissors':
            print("Cpu : Stone ")
            print("You : Scissors ")
            antip += 1
            print("You:", p, "CPU:", antip)
    elif i == 'paper':
        if move == 'stone':
            print("Cpu : Paper ")
            print("You : Stone ")
            print("CPU wins this point")
            antip += 1
            print("You:", p, "CPU:", antip)
        if move == 'paper':
            print("Cpu : Paper ")
            print("You : Paper ")
            print("No points play again")
            print("You:", p, "CPU:", antip)
        if move == 'scissors':
            print("Cpu : Paper ")
            print("You : Scissors ")
            print("This point goes to you")
            p += 1
            print("You:",p,"CPU:",antip)
    elif i == 'scissors':
        if move == 'stone':
            print("Cpu : Scissors ")
            print("You : Stone ")
            print("This point goes to you")
            p += 1
            print("You:", p, "CPU:", antip)
        if move == 'paper':
            print("Cpu : Scissors ")
            print("You : Paper ")
            print("CPU wins this point")
            antip += 1
            print("You:", p, "CPU:", antip)
        if move == 'scissors':
            print("Cpu : Scissors ")
            print("You : Scissors ")
            print("No points play again")
            print("You:", p, "CPU:", antip)
if p == 4:
    print(name,"won the match")
else:
    print("CPU won the match")
end =input("Now press 1 to exit")

