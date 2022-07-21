"""
TASK 1
"""

class CashRegister:

    def __init__(self):
        self.total_items = {}
        self.total_price = 0
        self.discount = 0

    def add_item(self, purchase_item):
        self.purchase_item = purchase_item
        self.total_items.update(self.purchase_item)
        item_price = list(purchase_item.values())[0]
        item_description = list(purchase_item.keys())[0]
        self.total_price += item_price
        print("Added the following item to your transaction:")
        print(f"{item_description}: £{item_price}")

    def remove_item(self, item_to_remove):
        self.item_to_remove = item_to_remove
        removed_item_price = self.total_items.get(item_to_remove)
        removed_item_description = item_to_remove
        self.total_items.pop(item_to_remove)
        self.total_price -= removed_item_price
        print("Removed the following item to your transaction:")
        print(f"{removed_item_description}: £{removed_item_price}")


    def apply_discount(self, discount_percentage):
        print(f"Discount percentage applied to the overall total: {discount_percentage} %")
        discounted_total = self.total_price * ((100 - discount_percentage)/100)
        formatted_discounted_total = "{:.2f}".format(discounted_total)
        print(f"Updated total: £{formatted_discounted_total}")


    def get_total(self):
        print(f"Your overall total: £{self.total_price}")

    def show_items(self):
        list_of_items = list(self.total_items.keys())
        print("Items added to your transaction so far:")
        for item in list_of_items:
            item_price = self.total_items.get(item)
            print(f"{item}: £{item_price}")

    def reset_register(self):
        self.total_price = 0
        self.total_items.clear()
        print("Please scan your first item.")

#Example code run:
transaction = CashRegister()
transaction.add_item({'Socks': 3.99})
# transaction.add_item({'Pear': 1.99})
# transaction.add_item({'Grapes': 2.99})

# transaction.show_items()

# transaction.get_total()
# transaction.apply_discount(39)

# transaction.remove_item('Socks')
# transaction.get_total()
#
# transaction.reset_register()
# transaction.get_total()

"""
Explanation for code above:
- 
"""

"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)


