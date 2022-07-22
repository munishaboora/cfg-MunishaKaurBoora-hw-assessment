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
        print(f"Discount percentage applied to the overall total: {discount_percentage} %")
        self.total_price = self.total_price * self.discount
        discounted_total = self.total_price
        formatted_discounted_total = "{:.2f}".format(discounted_total)
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
# transaction = CashRegister()
# transaction.add_item({'Socks': 4.00})
# transaction.add_item({'Pear': 2.00})
# transaction.add_item({'Grapes': 3.00})

# transaction.show_items()

# transaction.get_total()
# transaction.apply_discount(50)

# transaction.remove_item('Socks', 50)
# transaction.get_total()

# transaction.reset_register()
# transaction.get_total()

"""
Explanation for code above:
- 
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

    def show_student_details(self):
        print(f"ID number: {self.id }")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student assignments and marks:")
        print(f"Student assignments and marks:")


    def add_subject_and_grade(self, add_subject):
        self.subjects.update(add_subject)
        print(f"{self.subjects }")
        # print(f"{self.name}'s have been updated.")


    def remove_subject_and_grade(self, remove_subject):
        self.subjects.pop(remove_subject)
        print(f"{self.subjects }")

    def show_all_subjects(self):
        list_of_subjects = list(self.subjects.keys())
        print(f"Subjects and grades in {self.name}'s database:")
        for subject in list_of_subjects:
            subject_grade = self.subjects.get(subject)
            print(f"{subject}: {subject_grade}")

    def calculate_overall_mark(self):
        list_of_subjects = list(self.subjects.keys())
        print(f"Subjects and grades in {self.name}'s database:")
        number_of_subjects = 0
        overall_grades_total = 0
        for subject in list_of_subjects:
            number_of_subjects += 1
            overall_grades_total += self.subjects.get(subject)
        overall_grades_average = round(overall_grades_total / number_of_subjects)
        print(f"{self.name}'s overall average grade: {overall_grades_average}")

sarah = CFGStudent('Sarah', 23, 24)
sarah.add_subject_and_grade({'Homework 1': 95})
sarah.add_subject_and_grade({'Homework 2': 89})
sarah.add_subject_and_grade({'Homework 3': 98})
sarah.add_subject_and_grade({'Homework 4': 99})
sarah.show_all_subjects()
sarah.calculate_overall_mark()
# sarah.remove_subject_and_grade('Homework 2')
sarah.show_all_subjects()
# sarah.show_student_details()

# jasmine = CFGStudent('Jasmine', 27, 4)
# jasmine.add_subject_and_grade({'Homework 1': 56})
# jasmine.add_subject_and_grade({'Homework 2': 76})
# jasmine.add_subject_and_grade({'Homework 3': 91})
# jasmine.add_subject_and_grade({'Homework 4': 79})
# jasmine.show_all_subjects()
# jasmine.calculate_overall_mark()

# jasmine.remove_subject_and_grade('Homework 4')
# jasmine.show_all_subjects()
# jasmine.show_student_details()

"""
Explanation for code above:
- 
"""