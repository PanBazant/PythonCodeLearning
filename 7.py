import random
from hangman_words import word_list
from hangman_art import *


#word_list = ["ardvark", "baboon", "camel"]
print(logo)
chosen_word = random.choice(word_list)
display =  [ "_" for i in range(len(chosen_word))]
lives = 6
incorrect_char = []
print(f"The solution is {chosen_word}")


game = True
while game:
    if incorrect_char:
        print(incorrect_char)
    user_char = input("Write a character").lower()
    if user_char in display:
        print("You already guess this character")
        continue

    letter_index = 0
    for letter in chosen_word:
        if user_char == letter:
            print("This character is in the word")
            print(letter)
            display[letter_index] = letter
        else:
            print("This character is not in the word")
            if user_char not in incorrect_char and user_char not in chosen_word:
                incorrect_char.append(user_char)
       
        letter_index +=1
    if user_char not in chosen_word:   
        lives -= 1
    print(display)
    print(lives)
    print(stages[lives])
    if "_" not in display:
        game = False
        print("You win")
    if lives == 0:
        game = False
        print("You lose")