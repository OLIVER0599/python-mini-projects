"""
main.py
handles logic for quiz game
Features:
- provides questions
- tallys and calculates score
- provides starting (explanation) and ending (scoreboard) information
"""
import json

# open questions
def opened_questions_file():
    filename = 'src/questions.json'
    # open and closse safely
    try:
        with open(filename) as file: #
            questions = json.load(file)
            return questions
    except FileExistsError:
        print(f"file {filename} doesnt exist")
    except FileNotFoundError:
        print(f"file {filename} doesnt exist")
    except json.JSONDecodeError:
        print(f"the file {filename} is not a valid JSON file")
    except Exception as error:
        print(f"an unexpected error has occurred: {error}")
questions = opened_questions_file() #receive questions dict

# process questions, 
def main(questions):
    # provide explanation for game
    score = 0
    print(f"WELCOME TO THE QUIZ.\n\n enter only the first letter a, b c, d. \ngood luck!\n\n\n")

    for q in questions:

        # establish boolean for whether answer is right or not
        result = False
        # establish correct answer
        a = q['answer'].lower()
        correct_answer = a[0].strip()

        # receive answer
        print(f"{q['question']}")
        for option in q['options']:
            print(option)
        
        # check if answer given is valid
        while True:
            response = input(f"your answer? \n").lower().strip()
            if response:
                break
            else:
                print("no answer was given. please try again")
        
        # check if right
        if response == correct_answer:
            print(f"answer {response} is correct!")
            score +=1
        else:
            print(f"{response} was incorrect. the answer is {correct_answer}")
    
    print(f"you got {score} out 20 questions correct")
main(questions)





        






