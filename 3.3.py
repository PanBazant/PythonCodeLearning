print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S,M,L")
add_pepperoni = input("Do you want pepperoni? Y,N ")
extra_cheese = input("Do you want extra cheese? Y,N ")

cost = 0

if extra_cheese == "Y":
    cost += 1

if size == "S":
    cost = 15

if add_pepperoni == "Y":
    if size == "S":
        cost += 2
    else:
        cost += 3
 

elif size == "M":
    cost = 20

elif size == "L":
    cost = 25
else:
    print("Your pizza size is not correct")


     