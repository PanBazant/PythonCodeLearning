import random 
moves = ["rock", "paper", "scissors"]
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
computer_choose = random.randint(0,2)
print(f"You chose {moves[choose]}")
print(f"Computer chose {moves[computer_choose]}")
print(choose)
print(computer_choose)

if choose == computer_choose:
    print("It's a draw")

elif choose == 0 and computer_choose == 1:
    print("You lose")
elif choose == 1 and computer_choose == 2:
    print("You lose")
elif choose == 2 and computer_choose == 0:
    print("You lose")
else:
    print("You win")


