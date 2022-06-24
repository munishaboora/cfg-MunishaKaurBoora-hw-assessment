"""Homework 4"""
"""TASK 1 (Git and GitHub)"""
###Question 1###
"""
GIT WORKFLOW FUNDAMENTALS
· Working Directory - 
· Staging Area - 
· Local Repo (head) - 
· Remote repo (master) - 

WORKING DIRECTORY STATES:
· Staged - 
· Modified - 
· Committed - 

GIT COMMANDS:
· Git add - 
· Git commit - 
· Git push - 
· Git fetch - 
· Git merge - 
· Git pull - 
"""



"""TASK 2 (Exception Handling)"""
###Question 1###
#Task 1
correct_pin_code = 1234
pin_code = int(input("Please enter your pin code."))

#Task 2
def validate_pin(pin_code):
    correct_pin_code = 1234

    if pin_code != correct_pin_code:
        incorrect_pin_count = 1
        for num in range(2):
            pin_code = int(input("Please enter your pin code again."))
            if pin_code != correct_pin_code:
                incorrect_pin_count += 1
            else:
                break
        if incorrect_pin_count == 3:
            raise ValueError("Incorrect pin entered 3 times. Maximum limit reached.")


correct_pin = False
try:
    pin_code = int(input("Please enter your pin code."))
    validate_pin(pin_code)
except ValueError:
    print("Incorrect pin code entered 3 times.")
else:
    correct_pin = True
    print("Correct pin code entered.")
finally:
    if correct_pin:
        print("Please select your desired operation:")
    else:
        print("Card blocked.")

#Task 3
account_balance = 100

#Tasks 4 - 7
account_balance = 100
def validate_available_balance(withdrawal_amount):
    if withdrawal_amount > account_balance:
        raise ValueError("Insufficient funds available.")

try:
    withdrawal_amount = int(input("Please enter withdrawal amount."))
    validate_available_balance(withdrawal_amount)
except ValueError:
    print("Please either deposit funds into your account or withdraw a lesser amount.")
else:
    account_balance -= withdrawal_amount
    print(f"Remaining balance: £{account_balance}")
    print("Please take your cash with you.")



"""TASK 3 (Testing)"""
#Question 1

