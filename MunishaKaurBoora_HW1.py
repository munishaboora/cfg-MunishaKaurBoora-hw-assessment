"""
TASK 1
"""

class CashRegister:

    def __init__(self):
        self.total_items = {}
        self.total_price = 0
        self.discount = 0

    def add_item(self, purchase_item):
        self.total_items.update(purchase_item)

        item_price = list(purchase_item.values())[0]
        formatted_item_price = "{:.2f}".format(item_price)
        item_description = list(purchase_item.keys())[0]

        self.total_price += item_price

        print("Added the following item to your transaction:")
        print(f"{item_description}: £{formatted_item_price}")

    def remove_item(self, item_to_remove, discount_percentage_applied_to_transaction):
        removed_item_price = self.total_items.get(item_to_remove)
        removed_item_price_after_discount = (removed_item_price * ((100 - discount_percentage_applied_to_transaction)/100))
        formatted_removed_item_price = "{:.2f}".format(removed_item_price_after_discount)
        removed_item_description = item_to_remove

        self.total_items.pop(item_to_remove)
        self.total_price -= removed_item_price_after_discount

        print("Removed the following item to your transaction:")
        print(f"{removed_item_description}: £{formatted_removed_item_price}")


    def apply_discount(self, discount_percentage):
        self.discount = ((100 - discount_percentage)/100)
        self.total_price = self.total_price * self.discount

        discounted_total = self.total_price
        formatted_discounted_total = "{:.2f}".format(discounted_total)

        print(f"Discount percentage applied to the overall total: {discount_percentage} %")
        print(f"Updated total: £{formatted_discounted_total}")


    def get_total(self):
        formatted_total_price = "{:.2f}".format(self.total_price)

        print(f"Your overall total: £{formatted_total_price}")

    def show_items(self):
        list_of_items = list(self.total_items.keys())

        print("Items added to your transaction so far:")
        for item in list_of_items:
            item_price = self.total_items.get(item)
            formatted_item_price = "{:.2f}".format(item_price)

            print(f"{item}: £{formatted_item_price}")

    def reset_register(self):
        self.total_price = 0
        self.total_items.clear()

        print("Please scan your first item.")

#Example code run:
transaction = CashRegister()
   #Code to add an item to the transaction
transaction.add_item({'Socks': 3.00})
transaction.add_item({'Pear': 2.00})
transaction.add_item({'Grapes': 3.00})

   #Code to show all items in the transaction
transaction.show_items()

   #Code to apply a discount and then test that the discount has indeed been applied
transaction.apply_discount(50)
transaction.get_total()

   #Code to remove an item from a transaction and then test that the item has indeed been removed
transaction.remove_item('Socks', 50)
transaction.show_items()
transaction.get_total()

   #Code to clear a transaction from the register and then test that the items have all been removed
transaction.reset_register()
transaction.show_items()
transaction.get_total()

"""
Explanation for code above:
- For task 1, I used the class template provided and made one alteration to the __init__ function. I set self.total_items equal to {} so that each time an item is 'scanned', the items and their respective prices are stored as key:value pairs in a single dictionary.
- To the add_item class method, I passed purchase_item as a parameter so that each time an item is 'scanned', a dictionary containing a single key:value pair must be passed to the add_item method. This dictionary being passed would contain the name of the item, as a key, and its corresponding price, as a value.
      - Within the add_item class method, I've used the .update() method to update the dictionary of all items in the __init__ function with the key:value pair passed to the add_item class method.
      - Within the add_item class method, I've created the variables: item_price, formatted_item_price and item_description. item_price stores the value of the single key:value pair passed to the add_item class method. formatted_item_price is used to format the value stored in item_price to two decimal places. item_description stores the key of the single key:value pair passed to the add_item class method.
      - In the following line of code, I've added the value stored in the item_price variable to the overall total in the __init__ function.
      - Finally, I've used print statements to display the item's description and the formatted price in the console.

- To the remove_item class method, I passed item_to_remove and discount_percentage_applied_to_transaction as parameters. item_to_remove allows one to specify the key of the item to be removed from the transaction. discount_percentage_applied_to_transaction allows the correct amount to be deducted from total_price in the __init__ function - the discount percentage passed to the remove_item class method would depend on whether or not discount had been applied to a transaction to begin with. 
      - Within the remove_item class method, I've created a variable called removed_item_price and used the .get() method to return the value of the key that will be passed to the remove_item method.
      - Within the remove_item class method, I've created a variable called removed_item_price_after_discount to store the item's price after the discount percentage passed to the remove_item class method has been applied.
      - Within the remove_item class method, I've created a variable called formatted_removed_item_price to format the value stored in removed_item_price_after_discount to two decimal places.
      - Within the remove_item class method, I've created a variable called removed_item_description which I set equal to item_to_remove as I felt that the variable name removed_item_description was more clear.
      - In the following two lines of code, I have used the .pop() method to remove the key-value pair of the specified key from the dictionary in the __init__ function. I have then deducted the removed item's price from the overall total in the __init__ function.
      - Finally, I've used print statements to display the removed item's description and the removed item's formatted price.
 
- To the apply_discount class method, I passed discount_percentage as a parameter. discount_percentage allows a discount percentage to be passed to the apply_discount class method so that a discount can be applied to the overall transaction.
      - Within the apply_discount class method, I've amended the discount in the __init__ function based on the percentage passed to the apply_discount class method.
      - I've also adjusted the overall total in the __init__ function so that the overall total suggests that a discount has been applied.
      - Within the apply_discount class method, I've created a variable called discounted_total which I set equal to the overall total in the __init__ function as I felt that the variable name discounted_total was more clear.
      - In the following line of code, I've created a variable called formatted_discounted_total. I've formatted the value stored in discounted_total to two decimal places and stored it in formatted_discounted_total.
      - Finally, I've used print statements to display the discount percentage and the overall total after discount.

- Explanation of the get_total class method:
      - Within the get_total class method, I've created a variable called formatted_total_price to store the overall total in the __init__ function, formatted to two decimal places.
      - I've then created a print statement to output the formatted price to the console.
        
- Explanation of the show_items class method:        
      - Within the show_items class method, I've created a list of the keys in the dictionary in the __init__ function. I've stored this list in the variable list_of_items.
      - I've used a print statement to output some text to the console (for clarification on what is happening).
      - I've then used a for loop to iterate through the elements of the list stored in list_of_items. 
            - Within the for loop, I've used the .get() method to return the value of the key specified. The value would be retrieved from from the dictionary in the __init__ function.
            - I've then created a variable formatted_item_price which stores the value retrieved from the dictionary in the __init__ function, formatted to two decimal places.
      - Finally, I've created a print statement to output all the items in the transaction so far and their corresponding prices.    
            
- Explanation of the reset_register class method:  
      - Within the reset_register class method, I've set the overall total in the __init__ function equal to zero.
      - Within the reset_register class method, I've used the .clear() method to empty the dictionary in the __init__ function of its elements.
      - Finally, I've created a print statement to prompt an individual to scan an item (as the register has been cleared).
      
- Below the class, I've created a new object instance of the CashRegister class. The code for this is 'transaction = CashRegister()'.
      - I've then called the various methods within the class to test that the methods do indeed work.
"""




"""
TASK 2
"""

class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

class CFGStudent(Student):

    def add_subject_and_grade(self, add_subject):
        self.subjects.update(add_subject)
        subject_name = list(add_subject.keys())[0]

        print(f"Added the grade for {subject_name} to {self.name}'s database.")


    def remove_subject_and_grade(self, remove_subject):
        self.subjects.pop(remove_subject)

        print(f"Removed {remove_subject} from {self.name}'s database.")


    def show_all_subjects(self):
        list_of_subjects = list(self.subjects.keys())

        print(f"Subjects and grades in {self.name}'s database:")
        for subject in list_of_subjects:
            subject_grade = self.subjects.get(subject)

            print(f"{subject}: {subject_grade}")

    def calculate_overall_mark(self):
        list_of_subjects = list(self.subjects.keys())
        number_of_subjects = 0
        overall_grades_total = 0

        for subject in list_of_subjects:
            number_of_subjects += 1
            overall_grades_total += self.subjects.get(subject)

        overall_grades_average = round(overall_grades_total / number_of_subjects)

        print(f"{self.name}'s overall average grade: {overall_grades_average}")




sarah = CFGStudent('Sarah', 23, 24)
   #Code to add a subject and its grade
sarah.add_subject_and_grade({'Homework 1': 93})
sarah.add_subject_and_grade({'Homework 2': 89})
sarah.add_subject_and_grade({'Homework 3': 98})
sarah.add_subject_and_grade({'Homework 4': 99})

   #Code to show all subjects
sarah.show_all_subjects()

   #Code to show and calculate average mark
sarah.calculate_overall_mark()

   #Code to remove a subject and its corresponding grade and then verify that it has been removed
sarah.remove_subject_and_grade('Homework 1')
sarah.show_all_subjects()


jasmine = CFGStudent('Jasmine', 27, 4)
   #Code to add a subject and its grade
jasmine.add_subject_and_grade({'Homework 1': 56})
jasmine.add_subject_and_grade({'Homework 2': 76})
jasmine.add_subject_and_grade({'Homework 3': 91})
jasmine.add_subject_and_grade({'Homework 4': 79})

   #Code to show all subjects
jasmine.show_all_subjects()

   #Code to show and calculate average mark
jasmine.calculate_overall_mark()

   #Code to remove a subject and its corresponding grade and then verify that it has been removed
jasmine.remove_subject_and_grade('Homework 4')
jasmine.show_all_subjects()

"""
Explanation for code above:
- For task 2, I used the Student class template provided and made no alterations to it.
- I have created a new class called CFGStudent. 
      - I have passed the parent class, Student, as a parameter to the child class, when I created the new class called CFGStudent. This allows the CFGStudent class to inherit all the methods and properties from the Student class.

- Explanation of the add_subject_and_grade class method:  
      - Within the add_subject_and_grade class method, I've used the .update() method to update the dictionary in the __init__ function of the parent class with the key:value pair passed to the add_subject_and_grade class method.
      - I've created a variable called subject_name. subject_name is used to store the key of the key:value pair passed to the add_subject_and_grade class method.
      - The key description stored in subject_name has been used in a print statement to output a message verifying that a student's database has been updated to the console.

- Explanation of the remove_subject_and_grade class method:  
      - I have used the .pop() method to remove the key-value pair of the specified key from the subjects dictionary in the __init__ function of the parent class.
      - Finally, I've used a print statement to display a message in the console verifying that the details for the specified subject have indeed been removed.

- Explanation of the show_all_subjects class method:  
      - I've created a list_of_subjects variable to store a list of all of the keys in the subjects dictionary in the __init__ function of the parent class.
      - I've used a print function to output a message to the console.
      - I've then used a for loop to iterate through the elements of the list stored in list_of_subjects. 
            - I've created a variable called subject_grade and used the .get() method to return the value of the key specified in the subject_grade variable.       
            - I've used a print function to output each subject and its corresponding grade to the console.

- Explanation of the calculate_overall_mark class method:  
      - I've created a list_of_subjects variable to store a list of all of the keys in the subjects dictionary in the __init__ function of the parent class.
      - I've created the variable number_of_subjects as a counter to count the number of subjects in the dictionary in the __init__ function of the parent class.
      - I've created the variable overall_grades_total so that I can add the grades of all subjects, in the dictionary in the __init__ function of the parent class, to the variable one by one.
      - I've then used a for loop to iterate through the elements of the list stored in list_of_subjects. 
            - As I iterate through each of the elements, I add one to the variable number_of_subjects and a subject's grade to the variable overall_grades_total.
      - I've created a variable called overall_grades_average which is used to store the average of all subject grades for a particular student.
      - I've used a print function to output a message regarding the student's average grade to the console.

- Below the class, I've created two new object instances of the CFGStudent class. The code for this is 'sarah = CFGStudent('Sarah', 23, 24)' and 'jasmine = CFGStudent('Jasmine', 27, 4)'.
      - I've then called the various methods within the CFGStudent class to test that the methods do indeed work. I have done this for the two different students.
"""