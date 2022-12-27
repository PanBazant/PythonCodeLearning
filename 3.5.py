print("Welcome to Treasure Island\nYour mission is to find the treasure")
choice = input("left or right?\n")
if choice == "right":
    print("game over")
elif choice == "left":
    choice = input("swim or wait?\n")
    if choice == "swim":
        print("game over")
    elif choice == "wait":
        choice = input("Which door?")
        if choice == "blue":
            print("game over")
        elif choice == "red":
            print("game over")
        elif choice == "yellow":
            print("You win!")

else:
    print("Please write correct answer")