"""Homework 4"""
"""TASK 1 (Git and GitHub)"""
###Question 1###
"""
GIT WORKFLOW FUNDAMENTALS
· Working Directory - also known as working tree, consists of the files that one is currently working on i.e. one's project folder.
· Staging Area - The staging area is a file which is generally contained in your Git directory. The file stores information regarding what goes into your next commit. 
· Local Repo (head) - a Git repository that is stored on one's computer. When working with Git, only one branch can be checked out at a time - and this is what's called the 'HEAD' branch. 
· Remote repo (master) - a repository which is stored in a server. The default branch name in Git is master, however, GitHub renamed the master branch to main for any Git repository.

WORKING DIRECTORY STATES:
· Staged - means that one has marked a modified file, in its current version, to go into the next commit snapshot.
· Modified - means that you have changed a file but not yet committed it to your database.
· Committed - a file that is committed is that has the changes made to it safely stored in a snapshot in the Git directory. To commit a file, one uses the git commit command.

GIT COMMANDS:
· Git add - adds new or altered files, that are in your working directory, to the staging area. 
     - For example, git add [filename] selects a specific file, and moves it to the staging area, for inclusion in the next commit. 
     - git add., on the other hand, stages all files in the entire repository (provided that they are not listed in the .gitignore file).
· Git commit - provides a snapshot of one's repository (project) at a specific time.
     - For example, git commit only starts the commit process.
     - git commit -m "Enter message here" both starts the commit process and allows the inclusion of a  commit message.
· Git push - uploads all local branch commits to the corresponding remote branch.
· Git fetch - git fetch [remote] fetches changes from the remote, but does not update tracking branches.
· Git merge - git merge [branch] joins the specified branch into one's current branch.
· Git pull - updates one's present local working branch, and all remote tracking branches too. 
"""



"""TASK 2 (Exception Handling)"""
###Question 1###
#Task 1
# correct_pin_code = 1234
# pin_code = int(input("Please enter your pin code."))

#Task 2
# def validate_pin(pin_code):
#     correct_pin_code = 1234
#
#     if pin_code != correct_pin_code:
#         incorrect_pin_count = 1
#         for num in range(2):
#             pin_code = int(input("Please enter your pin code again."))
#             if pin_code != correct_pin_code:
#                 incorrect_pin_count += 1
#             else:
#                 break
#         if incorrect_pin_count == 3:
#             raise ValueError
#
#
# correct_pin = False
# try:
#     pin_code = int(input("Please enter your pin code."))
#     validate_pin(pin_code)
# except ValueError:
#     print("Incorrect pin code entered 3 times.")
# else:
#     correct_pin = True
#     print("Correct pin code entered.")
# finally:
#     if correct_pin:
#         print("Please select your desired operation:")
#     else:
#         print("Card blocked.")

#Task 3
# account_balance = 100

#Tasks 4 - 7
# account_balance = 100
# def validate_available_balance(withdrawal_amount):
#     if withdrawal_amount > account_balance:
#         raise ValueError("Insufficient funds available.")
#
# try:
#     withdrawal_amount = int(input("Please enter withdrawal amount."))
#     validate_available_balance(withdrawal_amount)
# except ValueError:
#     print("Please either deposit funds into your account or withdraw a lesser amount.")
# else:
#     account_balance -= withdrawal_amount
#     print(f"Remaining balance: £{account_balance}")
#     print("Please take your cash with you.")



"""TASK 3 (Testing)"""
#Question 1
'''
 - I have refactored the code in task 2 and changed the names of the functions, from validate_available_balance and validate_pin, to validating_available_balance and validating_pin respectively.
    - I've used the original code within the the validate_available_balance function and included the account_balance variable within the function. I've also added an else statement with a return statement, and a retrun sgtaement in place of the raise statement so that I am able to test the code.
 - In addition to testing the two refactored functions, I've also tested the original function validate_pin. The only alterations I've made to the validate_pin fucntion below is the addtion of a return statement and the pin_code variable which requests a pin from the user. 

 - Please refer to the testing_balance.py file for the unit tests corresponding to the validating_available_balance() function.
 - Please refer to the testing_pin.py file for the unit tests corresponding to the validating_pin() function.
 - Please refer to the testing_pin_original_function.py file for the unit tests corresponding to the validate_pin() function.
'''

def validating_available_balance(withdrawal_amount):
    account_balance = 100
    if withdrawal_amount > account_balance:
        return "Insufficient funds available."
    else:
        return "Sufficient funds available."

def validating_pin(pin_code):
    correct_pin_code = 1234

    if pin_code != correct_pin_code:
        return "Please enter your pin code again."
    else:
        return "Correct pin entered"

def validate_pin(pin_code):
    correct_pin_code = 1234

    pin_code = int(input("Please enter your pin code."))
    if pin_code != correct_pin_code:
        incorrect_pin_count = 1
        for num in range(2):
            pin_code = int(input("Please enter your pin code again."))
            if pin_code != correct_pin_code:
                incorrect_pin_count += 1
            else:
                return "Correct pin entered."
        if incorrect_pin_count == 3:
            raise ValueError

