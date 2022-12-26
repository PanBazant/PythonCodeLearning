print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
amount_of_people = int(input("How many people to split the bill? "))

bill_for_person = round((bill + bill * (tip / 100)) / amount_of_people, 2)

print("Each person should pay: ${}".format(bill_for_person))

