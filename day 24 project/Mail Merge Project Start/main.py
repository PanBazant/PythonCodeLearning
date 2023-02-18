#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter_template = ""
guest_list = []

with open("day 24 project/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    letter_template = file.read()

with open("day 24 project/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    #print(file.read())
    #print(file.read().split("\n"))
    for i in file.read().split("\n"):
        guest_list.append(i)

print(guest_list)
#print(letter_template.replace("[name]", "imie"))

for i in guest_list:
    with open(f"day 24 project/Mail Merge Project Start/Output/ReadyToSend/letter_for_{i}.txt", "w") as f:
        f.write(letter_template.replace("[name]", i))