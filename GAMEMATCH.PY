print("Now you are ready to play the game, let's start with the first match!")
print("You are playing against the computer, let's see how you do!")
user = input("Heads or Tails? Type heads or tails to choose")
if user == "heads":
    print("You have chosen heads, let's flip the coin!")
if user == "tails":    print("You have chosen tails, let's flip the coin!")
import random
coin = random.choice(["heads", "tails"])

if user == coin:
    print("Congratulations! You won the toss, you can choose to bat or bowl first.")
else:    print("Sorry, you lost the toss, the computer will choose to bat or bowl first.")
