"""
Budget Tracker
Tracks expencse, show bugdget details 

Takes in (Initital Budget) one time
(expense), (budget details) recurring through while loop
(exit)feature one time
"""

import json

def add_expenses(description, expense, budget, expenses):
    """make expense positive value, expenses is a list, budget a float, description a string"""
    budget -= expense
    expenses.append({"description": description, "expense": expense, "budget": budget})
    print(f"Added exepense: {description}, amount: {expense}")

def current_balance(initial_budget, total_expenses):
    balance = initial_budget - total_expenses
    return balance

def total_expenses(expenses):
    total_expenses = 0
    for expense in expenses:
        total_expenses += expense['expense']
    return total_expenses

def show_budget(initial_budget, budget, expenses):
    # print current budget
        print(f"Initial Budget: {initial_budget} \nCurrent Budget: {budget} \n")
        for expense in expenses:
            print(f"expense: {expense['description']}, amount: {expense['expense']}")

def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0,[]
def save_budget_data(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses,
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)



def main():
    # enter initial budget
    print("welcome to the budget tracker \n")
    filepath = 'budget_data.json'

    initial_budget, expenses = load_budget_data(filepath)
    if initial_budget == 0:
        initial_budget = float(input("enter the initial budget:  "))
    
   
    budget = initial_budget
    expenses = []

    while True:
        # provide 3 options

        print("press 1, 2 or 3 for the following options.")

        print("record expense? /1")
        print("show budget? /2")
        print("exit? /3")
        option = int(input("?: "))

        # expenses?
        if option == 1:
            description = input("enter description for expense: ")
            expense = float(input("enter the expense value: "))

            # record expense to expenses
            add_expenses(description, expense, budget, expenses)
            

        # show budget?
        elif option == 2:
            show_budget(initial_budget, budget, expenses)
            total = total_expenses(expenses)
            print(f"total expenses: {total}, current balance: {current_balance(initial_budget, total_expenses(expenses) )}")
            

        # exit?
        elif option == 3:
            # break
            save_budget_data(filepath, initial_budget, expenses)
            break

main()