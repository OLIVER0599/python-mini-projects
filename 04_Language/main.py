"""
main.py
process spanish quiz

Features:
- updates and saves score
- tests spanish words
"""
import json
import random

def load_score(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data.get("score", 0), data.get('words', [])
    except:
        return 0, []

def save_score(filepath, score):
    score_data = {
        "score": score
    }
    try:
        with open(filepath, 'w') as file:
            json.dump(score_data, file, indent = 4)
            
    except:
        print("error with saving score")

def main():

    # introduce game
    print("Welcome to the spanish quiz!!")
    start = input("press enter to start")
    
    # access data from json file safely as words pairs
    filepath = 'spanish_words.json'
    score, words = load_score(filepath)

    # shuffle the words
    random.shuffle(words)
    print(f"Your score to beat is: {score}")
    print("For each word given what is it in english. If you want to quit give 2 as an answer.")

    # process game
    for question in words:

        # what the spanish and correct english word is
        s_word = question["spanish"].lower().strip()
        e_word = question["english"].lower().strip()

        # ask for answer
        answer = input(f"what is the english word for {s_word}?  ").lower().strip()

        # allow for a break option 
        if answer == '2':
            print(f"You have given up. Your score is {score}") 
            save_score(filepath, score)
            return

        # is answer correct, if not minus 1 point. if so add one point
        elif answer == e_word:
            score +=1
            print("Correct!!! \n")

        elif answer != e_word:
            print(f"Incorrect!!!, the correct answer was: {e_word} \n")

main()






