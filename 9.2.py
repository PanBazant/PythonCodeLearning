#pythontutor.com/visualize

print("Welcome to the secret auction program.")
offer = {}
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    offer[name] = bid
    other = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other == "no":
        break

max_offer = 0
winner = ""
for i in offer:
    if offer[i] > max_offer:
        max_offer = offer[i]
        winner = i

print("The winner is {} with a bid of ${}".format(winner, max_offer))



