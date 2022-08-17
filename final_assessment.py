"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""
import random

class CFGStudent:

    def __init__(self, name, surname, age, email, student_id=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = self.generate_id()


    def generate_id(self):
        random_new_id = str(random.sample(range(1000, 10000), 1))[1:-1]
        return random_new_id

    def get_id(self):
        return f"{self.student_id}"

    def get_fullname(self):
        return f"{self.name} {self.surname}"


class NanoStudent(CFGStudent):

    def __init__(self, name, surname, age, email, specialization, student_id=None):
        super().__init__(name, surname, age, email, student_id=None)
        self.specialization = specialization
        self.course_grades = []


    def generate_id(self):
        return 'NANO' + super().generate_id()[1:-1]


    def add_new_grade(self, task_name, grade):
        name_and_grade =[task_name, grade]
        self.course_grades.extend(name_and_grade)

    def get_course_grades(self):
        for subject in self.course_grades:
            print(subject)
        # return self.course_grades.items()



############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# # returns 'Anna Smith'
print(s.student_id)
# # returns '3868' or some other random number

cfg_s = NanoStudent( name='Mia', surname='Papandopulu', age=20, email='mia@mail.com', specialization='Software')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""
def even_fibonacci_sum(limit):
    if limit == 0:
        return 0
    if limit == 1 or limit == 2:
        return 1
    else:
        return even_fibonacci_sum(limit-1) + even_fibonacci_sum(limit-3)

##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0





"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""


def is_valid_subsequence(array, sequence):
    sequence_index = 1

    for number in sequence:

        if number in array:
            index = array.index(number)
            array = array[index:]
            sequence = sequence[:sequence_index-1] + sequence[sequence_index:]

    return len(sequence) == 0


#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE



"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""

"""
Answer to task 4:

To improve the code in task 4, my classmate should look at the SOLID principles which when implemented properly, make one's code more extendible, logical and easier to read.
SOLID stands for:
- Single responsibility. Single responsibility means that a class should have only one job and therefore it should have only a single reason to change.
- Open - closed. Open - closed principle means that software entities, (Classes, modules, functions), should be open for extension, not modification.
- Liskov substitution. The liskov substitution principle states that if class A is a subtype of class B, then we should be able to replace B with A without disrupting the behavior of our program.
- Interface segregation: larger interfaces should be split into smaller ones. Doing this ensures that implementing classes only need to be concerned about the methods that are of interest to them.
- Dependency injection: dependency injection refers to the decoupling of software modules. This way, instead of high-level modules depending on low-level modules, both will depend on abstractions.


As the class Employee relates to an employee, it should only contain attributes related to an employee. Therefore the save_employee, print_employee_report and remove_employee methods, should be in another class instead.
In this sense, the class seems to break the single responsibility principle mentioned above. The save_employee and remove_employee methods should be placed in another class as they do not refer to characteristics of an employee such as one's name or age. 
They instead are actions that show alteration of an employee's data from a database or file.

- In the print_employee_report method, the individual has used the correct mode, w, as one would want to over write the data in the file with the new information obtained.
   - The individual has also correctly used writelines as it writes the contents of a list of strings to the file specified.
   
   
The code correctly follows the open-closed principle that that software entities, (Classes, modules, functions), should be open for extension, not modification. This is because one can extend the class using inheritance.
The code breaks the interface segregation principle because many methods unrelated to the employee specifically are included.

In order ot fix the code, one can make use of the print() function to test whether the code works as intended.   
"""







