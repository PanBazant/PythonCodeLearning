with open("day 24/my_file.txt") as file:
    content = file.read()
    print(content)

with open("new_file.txt", "w") as file:
    file.write("New text.")