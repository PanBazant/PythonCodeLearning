import random


print("Welcome to the PyPassword Generator!")

letters_char = [chr(x) for x in range(65, 91)]
letters_char.extend([chr(x) for x in range(97, 123)])
numbers_char = [str(x) for x in range(10)]
symbols_char = [chr(x) for x in range(33,47)]
print(symbols_char)


letters = int(input("How many letters would you like in your password? "))
symbols= int(input("How many symbols would you like? "))
numbers = int(input("How many numbers would you like? "))

print("Here is you password")


password = ""

for i in range(letters):
    password += random.choice(letters_char)
for i in range(symbols):
    password += random.choice(symbols_char)
for i in range(numbers):
    password += random.choice(numbers_char)

random.shuffle(list(password))

print(password)
