#### 1. How does Object-Oriented Programming differ from Process Oriented Programming?

- Object-Oriented Programming is a programming paradigm which relies on the concept of classes and objects.
    - It is used to structure a software program into simple, reusable pieces of code blueprints, usually referred to as
      classes.
    - The classes are normally used to create individual instances of objects.

- Process Oriented Programming is a programming paradigm in which the primary concerns are the process structure and
  communication between the processes of a system.

- The key differences between Object-Oriented Programming and Process Oriented Programming are:
    - Access specifiers
        - Object-Oriented Programming has access specifiers such as private, public, protected, etc.
        - Process Oriented Programming does not have access specifiers.
    - The approaches
        - Object-Oriented Programming follows a bottom-up approach.
        - Process Oriented Programming follows a top-down approach.
    - Adding new data and functions
        - In Object-Oriented Programming, adding new data and functions is relatively easy.
        - In Process Oriented Programming, adding new data and functions isn't easy.
    - Different usages
        - Object-Oriented Programming is used for designing complex and large programs.
        - Process Oriented Programming is used for designing medium-sized programs.
    - Code reusability
        - In Object-Oriented Programming, code reusability is present.
        - In Process Oriented Programming, code reusability is not present.
    - The division of the programs
        - In Object-Oriented Programming, the program is divided into small parts, referred to as objects.
        - In Process Oriented Programming, the program is divided into small parts, referred to as functions.

#### 2. What's polymorphism in OOP?

- Polymorphism is the condition of occurrence in different forms. 
- Polymorphism refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.
- Polymorphism is a concept in Python programming wherein an object defined in Python can be used in different ways.
- Polymorphism allows the programmer to define multiple methods in a derived class, and it has the same name as present in the parent class.
- Such scenarios support method overloading in Python.

- Example 1:
```commandline
class Lion:
    def diet(self):
        print("carnivore")


class Giraffe:
    def diet(self):
        print("herbivore")


object_lion = Lion()
object_lion.diet()

object_giraffe = Giraffe()
object_giraffe.diet()
```
Explanation for the code above:
- Above, I've created two new classes: Lion and Giraffe.
- The outputs from this program are carnivore and herbivore, respectively. 
- The two classes both use the method name diet, but they define the methods differently. 
- An object instantiated from the Lion class will use the method as it is defined in that class. 
- The Giraffe class may have a method with the same name, but objects instantiated from the Lion class won’t interact with it.
- This code above is an example of occurrence in different forms. 

- Example 2:
```commandline
class VehicleDetails:

    def __init__(self, brand, colour, model):
        self.brand = brand
        self.colour = colour
        self.model = model

    def print_vehicle_details(self):
        print(f"Vehicle brand: {self.brand}")
        print(f"Vehicle colour: {self.colour}")
        print(f"Vehicle model: {self.model}")

class Cycle(VehicleDetails):
    def print_vehicle_details(self):
        print(f"The cycle's brand is {self.brand} and its model name is {self.model}. The cycle is also {self.colour} in colour.")

class Car(VehicleDetails):
    def print_vehicle_details(self):
        print(f"The car's brand is {self.brand} and its model name is {self.model}. The car is also {self.colour} in colour.")


munishas_cycle = Cycle('Raleigh', 'blue', 'stowaway folding bike')
munishas_cycle.print_vehicle_details()

munishas_car = Car('BMW', 'purple', 'BMW X5')
munishas_car.print_vehicle_details()
```
Explanation for the code above:
- The child classes, Cycle and Car, inherit methods and attributes from the parent class, VehicleDetails.
- I can redefine certain methods and attributes specifically to fit the child classes above. This is known as Method Overriding.
- Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.
- Above, I have overridden the print_vehicle_details method from the parent class, VehicleDetails. 

#### 3. What's inheritance in OOP?

- Inheritance is the process by which one class takes on the attributes and methods of another. 
- Newly formed classes are called child classes.
- The classes that child classes are derived from are called parent classes. 
- Child classes can override or extend the attributes and methods of parent classes. 
- Child classes inherit the parent class' attributes and methods but can also specify attributes and methods that are unique to themselves.

```commandline
class VehicleDetails:

    def __init__(self, brand, colour, model):
        self.brand = brand
        self.colour = colour
        self.model = model

class Cycle(VehicleDetails):
    def print_cycle_details(self):
        print(f"Cycle brand: {self.brand}")
        print(f"Cycle colour: {self.colour}")
        print(f"Cycle model: {self.model}")

class Car(VehicleDetails):
    def print_car_details(self):
        print(f"Car brand: {self.brand}")
        print(f"Car colour: {self.colour}")
        print(f"Car model: {self.model}")


munishas_cycle = Cycle('Raleigh', 'Blue', 'Stowaway folding bike')
munishas_cycle.print_cycle_details()

munishas_car = Car('BMW', 'Purple', 'BMW X5')
munishas_car.print_car_details()
```
Explanation for the code above:
- The code above is an example of multiple inheritance as the parent class, VehicleDetails, inherits to multiple child classes, Cycle and Car.
- The Cycle and Car child classes take on the attributes and methods of the parent class, VehicleDetails.
- The child classes, Cycle and Car, are derived from the parent class, VehicleDetails.
- The child classes, Cycle and Car, extend the attributes of the parent class. For instance both classes use the brand, colour and model.
- The child classes inherit the parent class' attributes but can also specify methods that are unique to themselves. For instance, the Cycle class specifies the print_cycle_details method and the Car class specifies the print_car_details method.

#### 4. If you had to make a program that could vote for the top three funniest people in the office, how would you do that? How would you make it possible to vote on those people?
To make a program that could vote for the top three funniest people in the office, I would start by creating some user stories, for instance:
- As an employee working in the office, I want to be able to check who the funniest people in the office are, so that I know if I am considered to be funny.
- As a manager in the office, I want to be able to analyse the overall votes, so that I know which individuals to award a prize to.

- The first user story above essentially requires the ability for an employee to be able to check the cumulative votes. 
- The second user story above requires the office manager to be able to use the overall votes to reward employees. 

- As one can start writing the code for the backend or the frontend of a software in any order, all tasks above can be completed simultaneously, by three separate individuals in the development team.

- To build a simple prototype of a program that could vote for the top three funniest people in the office, I would follow the agile methodology because it helps analyse and improve products whilst they’re going through different phases of development. 
   - This methodology enables one to produce more valuable products for customers by following an incremental approach.
   
- Each sprint would last two weeks. A sprint is a short period of time when a scrum team works to complete a set amount of work.
- Each sprint would start with a sprint planning meeting - this would be conducted before every sprint and would be attended by the scrum master, the development team and the product owner. 
   - These individuals would all select the high priority items from the product backlog in such a way that the development team can deliver them in one single sprint. 
      - The list of selected items is known as the sprint backlog. The development team works on the sprint backlog throughout the sprint.
- During the sprint, every day, a daily scrum meeting is held. In this meeting each participant would answer 3 questions: what they did yesterday, what they'll do today, and the issues facing the developers.
- The outcome of the sprint would be a potentially shippable product. Whether or not the product is ready to be shipped depends on whether the product owner wants to ship the product or add more features to the product.
- Finally, after the sprint has taken place, the sprint review and sprint retrospective occur.
   - In the sprint review, the scrum team would showcase what it has accomplished during the sprint - this may include a demo of new features added to the product.
   - In the sprint retrospective, the team contemplate on what went well, what went badly and what could be improved. The objective of a sprint retrospective is to improve the sprints held in the future.

- I would make a program that could vote for the top three funniest people in the office with the help of a class as shown below.
   - Below, to cast a vote, the vote_for_a_person method would be called and passed a name.
   - To display the top 3 most funny people, the top_three_most_funny_individuals method must be called.
```commandline
from collections import Counter


class TopThreeMostFunnyIndividuals:
    def __init__(self):
        self.votes_received = []

    def vote_for_a_person(self, add_vote):
        self.votes_received.append(add_vote)

    def top_three_most_funny_individuals(self):
        votes_per_person = Counter(self.votes_received)
        three_most_funny_individuals_list = sorted(votes_per_person, key=votes_per_person.get, reverse=True)[:3]
        three_most_funny_individuals = ", ".join(three_most_funny_individuals_list)
        print(f"The top 3 most funny individuals in the class are: {three_most_funny_individuals}.")


vote = TopThreeMostFunnyIndividuals()

vote.vote_for_a_person('James')
vote.vote_for_a_person('Lisa')
vote.vote_for_a_person('James')
vote.vote_for_a_person('Louisa')
vote.vote_for_a_person('Sandy')
vote.vote_for_a_person('Lisa')
vote.vote_for_a_person('James')
vote.vote_for_a_person('Sandy')
vote.vote_for_a_person('Sandy')
vote.vote_for_a_person('Lisa')
vote.vote_for_a_person('Louisa')
vote.vote_for_a_person('James')
vote.vote_for_a_person('Joey')
vote.vote_for_a_person('James')
vote.vote_for_a_person('Louisa')
vote.vote_for_a_person('Joey')
vote.vote_for_a_person('Sandy')

vote.top_three_most_funny_individuals()
```

Some key requirements:
- A database to store a user's name, the number of votes they have, etc.
- A user interface that makes voting for an individual fast and simple.
- The framework to build the user interface and connect to the database.

Main considerations:
- Will the booking system be used for one office only or multiple offices operating under one company name?
- The options available for storing the data e.g Informix, MySQL, MongoDB, etc.
- How the booking system would deal with multiple people attempting to vote (as would be the case when voting for a popular individual).
- What will the UI look like?
- Do we need to support both web apps and mobile apps?

Common or biggest problems:
- Individuals not receiving confirmation of their vote being cast.
- Users accidentally voting for the wrong person or accidentally misspelling something.
- Users not wanting to use the website because they don’t like the user interface or it is too difficult to navigate.
- The website taking a long time to load, leading to the user becoming frustrated.
- How many options should be displayed to the user when casting a vote (a lot of options would be hard to display and may overwhelm the user).

Components or tools I would use:
- For the voting system, I would use a strategy design pattern as it requires choosing a specific implementation of an algorithm or task at run time – out of multiple other implementations for the same task.
- For the website design, I would use React JS. React JS is a JavaScript library for building user interfaces.
   - I would use React because it is all about splitting an application into small building blocks, where every building block, every component, has a clear task and therefore one's code stays maintainable and manageable.
- I would use the Django python web framework.
   - I would use Django as it is well known to be a high-performing web framework out of the box and it is used by extremely high-traffic apps. This framework would help deal with the issue of a lot of users attempting to cast a vote at the same time.

#### 5. What's the software development cycle?

- The software development cycle involves the application of standard business practices to the building of software
  applications.
- The software development cycle is typically broken down into the following steps: Planning, Requirements, Design,
  Implementation, Testing and Integration, Deploy, and Maintenance.
    - Planning: 
       - Leaders of the project evaluate the terms of the project, including the calculation of labour and material costs to create a timetable with goals. 
       - Planning would also include areas of feedback from stakeholders or anybody who is going to benefit from the application itself. 
       - At this stage, the scope of the project would be clearly defined, the purpose of the application would be outlined and the boundaries that are needed to keep the project from expanding beyond scope or shifting would be set.
    - Requirements: 
       - At this stage, requirements would be defined and documented and stakeholder approval would also be sought. 
       - What the application is meant to do, features to be included, and potential roadblocks would be defined. 
       - Resources would also need to be identified and built into the project in order to define requirements.
    - Design: 
       - At this step, how the application will work and aspects of the design are modelled. 
       - Some aspects can include: UI, Programming, Security, Architecture, etc.
    - Implementation: 
       - At this step, the program itself is written out, either using a single developer or a large team - with each working on different parts of the application. 
    - Testing and Integration: 
       - In this phase, a software implementation is packaged and tested to assure quality. 
       - Testing or quality assurance ensures the solutions implemented pass the standard for quality and performance. 
       - This can involve unit testing, performing integration and end-to-end tests, and reporting or identifying bugs or defects in the software solution.
    - Deploy: 
       - An application is deployed once testing is completed, making it available to users. 
       - This step of the process can be manual or automated, depending on the complexity and needs of the application.
    - Maintenance: 
       - Once the application has been deployed and is being used, the final phase discovers bugs that slipped through the cracks during testing and resolves them - this can spawn new development cycles.

#### 6. What's the difference between agile and waterfall?
- Agile methodology is an approach to software development that helps the continuous iteration of development and testing in the software development process. 
   - In this model, development and testing activities are concurrent. 
   - This process allows more communication between customers, developers, managers, and testers.

- The waterfall methodology is a project management approach that emphasises a linear progression from the beginning to the end of a project.  
   - In Waterfall, one stage of the workflow needs to be fully completed before moving on to the next one.

- The key differences between agile and waterfall:
    - Sprints versus phases
        - Agile: separates the project development lifecycle into sprints.
        - Waterfall: divides the software development process into distinct phases.
    - Changes to requirements 
        - Agile: has a flexible method which allows changes to be made to the project development requirements - even if the initial planning has been completed.
        - Waterfall: there is no scope to change the requirements once the project development starts.
    - Development approach
        - Agile: follows an iterative development approach, due to which the planning, development, prototyping and other software development phases may appear more than once.
        - Waterfall: the project development phases such as designing, development, testing, are completed once in the Waterfall model.
    - Requirements preparation
        - Agile: the product owner prepares the requirements with the team almost daily during a project.
        - Waterfall: business analysts prepare requirements before the beginning of the project.
    - Testing
        - Agile: testing is performed concurrently with software development.
        - Waterfall: the testing phase comes after the implementation phase.
    - Changes to project description
        - Agile: description of project details can be altered anytime during the software development process.
        - Waterfall: detailed description required to implement the waterfall methodology.

#### 7. What is a reduced function used for?
- In Python, the reduce() function is defined in the functools module. One must type 'from functools import reduce' before attempting to use the reduce function.
- The reduce() function receives two arguments, a function and an iterable. However, it doesn't return another iterable, instead it returns a single value.
- The reduce function is used to apply a particular function, passed in its argument, to all elements of the iterable, also passed in its argument.

```commandline
from functools import reduce

numbers = [0, 5, 10, 20, 30, 40]


def sum_up(a, b): 
    return a + b


result = reduce(sum_up, numbers) 
print(result)
```
Explanation for the code above:
- Above, I've imported reduce from the functools module so that I can later use the reduce function.
- I've created a variable called numbers and stored a list in it.
- I've also created a function, sum_up, which sums up two inputs.
- I've passed sum_up and numbers to a reduce function and stored the result in the variable result.
- The value stored in result is printed to the console using the print function.

```commandline
from functools import reduce

print(reduce(lambda a, b: a + b, [0, 5, 10, 20, 30, 40])) 
```
Explanation for the code above:
- Above, I've imported reduce from the functools module so that I can later use the reduce function.
- I've created a lambda function which sums two inputs and returns their sum.
- I've passed the lambda function to the reduce function and also passed a list to the reduce function too.
- I've then printed out the result of the reduce function to the console.

#### 8. How does merge sort work?
- Merge sort is one of the most prominent divide-and-conquer sorting algorithms. It can be used to sort the values in any traversable data structure such as a list.
- Merge sort works by splitting the input list into two halves, repeating the halving process on those halves, and finally merging the two sorted halves together.
- The algorithm first moves from top to bottom, dividing the list into smaller and smaller parts until only the separate elements remain. 
- From there, it moves back up, ensuring that the lists to be merged are sorted.
- The algorithm works in O(nlogn). This is because the list is being split in log(n) calls and the merging process takes linear time in each call.

- Below is an example of the implementation of the merge sort algorithm (the recursive approach for implementing merge sort):
```commandline
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)
```
Explanation for the code above:
- The list is divided into left and right in each recursive call until two adjacent elements are obtained. 
- The i and j iterators traverse the two halves in each call. The k iterator traverses the whole lists and makes changes along the way. 
- If the value at i is smaller than the value at j, left[i] is assigned to the myList[k] slot and i is incremented. If not, then right[j] is chosen. This way, the values being assigned through k are all sorted. 
- At the end of this loop, one of the halves may not have been traversed completely. Its values are simply assigned to the remaining slots in the list.

#### 9. Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is a use case?
- Python provides a generator to create your own iterator function. 
- A generator is a special type of function which does not return a single value, instead, it returns an iterator object with a sequence of values. 
- In a generator function, a yield statement is utilised rather than the usual return statement. The yield statement returns a value and pauses the execution while maintaining the internal states.

- Example 1:
```commandline
def powers_of_four(items_length):
    n = 0
    while n < items_length:
        yield 4 ** n
        n += 1


my_iter = powers_of_four(5)

for i in my_iter:
    print(i)
```
Explanation for the code above:
- In the above example, the powers_of_four() function is a generator function. 
- It uses yield instead of the return keyword, thereby returning the value against the yield keyword each time it is called.
- Above, I've used a for loop to traverse the elements of the generator. In this case, the next() function is called implicitly and the StopIteration is also automatically taken care of.


 - Example 2:
```commandline
def print_elements(number_of_elements):
    n = 1
    while n < number_of_elements:
        yield f"Element number {n}."
        n += 1


generator = print_elements(4)

for i in generator:
    print(i)
```
Explanation for the code above:
- In the above example, the print_elements() function is a generator function. 
- It uses yield instead of the return keyword, thereby returning the value against the yield keyword each time it is called.
- Above, I've used a for loop to traverse the elements of the generator. In this case, the next() function is called implicitly and the StopIteration is also automatically taken care of.

#### 10. Decorators - A page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator?
- A decorator is a function that accepts a function and returns a function i.e. the return value of a decorator function must be the function used to wrap the function to be decorated. 
   - Python will take the returned function and call it at decoration time, passing the function to be decorated.
   - As a decorator returns a function, a decorator does not have a specific return type. 

- Using decorators is beneficial because they're reusable, they can be used on classes, they can be used to check if a user is logged in, etc.
1. As a decorator is just a regular Python function, all the usual tools for easy reusability are available. 
```commandline
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice


@do_twice
def say_hello():
    print("Hello!")


@do_twice
def say_bye():
    print("Bye!")

say_hello()
say_bye()
```
- When running the above example, the say_hello() function is executed twice and so is the say_bye() function. 
- 'Hello!' is outputted to the console twice, followed by 'Bye!' being outputted to the console twice too. 
- As shown above, the do_twice decorator can be used again and again. 

2. decorators can be used to decorate the methods of a class. 
   - Some commonly used decorators that are even built-ins in Python are @classmethod, @staticmethod, and @property. 
   - The @classmethod and @staticmethod decorators are used to define methods inside a class namespace that are not connected to a particular instance of that class. 
   - The @property decorator is used to customize getters and setters for class attributes. 

- Suppose we have two decorators, already created, called debug and timer, as below.
- Below is an example of how a decorator can be used on the method of a class, thereby changing the behaviour of the method when it is called.
```commandline
from decorators import debug, timer

class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
    
    tw = TimeWaster(1000)
    tw.waste_time(999)
            
```

3. Decorators can be used when working with a web framework. 
   - Below, Flask is being used to set up a /secret web page that should only be visible to users that are logged in or otherwise authenticated.

```commandline
from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    ...
```