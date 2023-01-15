import random

data = [["Rihanna", 30000], ["Shakira", 20000], ["Kot", 20], ["Pies", 50]]
score = 0
game = True

while game == True:
    first = random.choice(data)
    second = random.choice(data)
    while first == second:
        second = random.choice(data)
    print(second)

    player_choice = input("Who has more A:{} or B:{}".format(first[0], second[0]))
    if player_choice == "A":
        if first[1] > second[1]:
            score += 1
            data.remove(first)
            data.remove(second)

        else:
            print("You lose")
            game = False
    else:
        if second[1] > first[1]:
            score += 1
            data.remove(first)
            data.remove(second)
        else:
            print("You lose")
            game = False


print(data)
print(f"Your score are {score}")
