""" 
main.py
handles logic for hangman game

Features:
- selects a random word from a collection of words
- a series of underlines representing unkown letters of word
- accepts guesses which if
- correct: replaces the underlines with the correct letter in the right pos
- incorrect: reduces the amount attempts left
- loops until attempts are 0 or all letters have been guessed correctly
"""

# process list of words
def word_list():
    import os

    filename = os.path.join(os.path.dirname(__file__), 'src', 'words.txt')
    try:
        with open(filename) as file:
            contents = file.read()
            word_list = [word.strip(',\'\"').lower() for word in contents.split()]
            return word_list

    except FileExistsError:
        print(f"file doesnt exist. Expected file path: {filename}")
    except FileNotFoundError:
        print(f"file not found")
    except Exception as e:
        print(f"the error: ({e}) has occurred.")

    
    

def change_underlines(underlines, index, guess):
    underline_l = list(underlines)
    underline_l[index] = guess
    underlines_new = ''.join(underline_l)
    underlines_2 = underlines_new
    return underlines_2

# set up game 
words = word_list()

from random import *
chosen_word = choice(words)

underlines_list = ['_' for _ in chosen_word]
underlines = "".join(underlines_list)

print("Guess the Word \n Begin Hangman! \n")
print(underlines)

# process guesses (until attempts end or word is guessed)
attempts = 9
already_guessed = []
while (attempts>=0 and '_' in underlines):
    
    guess = input('your guess?: ')

    if guess not in already_guessed:
        if guess.isalpha():
            
            already_guessed.append(guess)
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    print("correct")

                    # perform function for changing underlines
                    underlines_new = change_underlines(underlines, index, guess)
                    underlines = underlines_new # set the string underliens as the new underlines

            if guess not in chosen_word:
                print(f"{guess} is wrong. Try again.")
        else:
            print('please make your guess a letter')
            continue
    else: 
        print(f"you have already guessed the letter {guess}")
            
    attempts -= 1
    print(underlines_new)
if attempts == 0:
    print(f"You have lost Better luck next Time. \n The correct word was: {chosen_word}")
if '-'  not in underlines:
    print(f"You have won!")
            

















