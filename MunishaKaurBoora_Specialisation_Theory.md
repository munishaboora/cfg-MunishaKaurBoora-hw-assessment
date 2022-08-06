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

- Polymorphism can be defined as a condition that occurs in many different forms.
- It is a concept in Python programming wherein an object defined in Python can be used in different ways.
- It allows the programmer to define multiple methods in a derived class, and it has the same name as present in the
  parent class.
- Such scenarios support method overloading in Python.

- Describe polymorphism and provide 2 examples ... Explain the exmaples

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

#### 3. What's inheritance in OOP?

- Describe inheritance and
- provide 2 examples ...

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

#### 4. If you had to make a program that could vote for the top three funniest people in the office, how would you do that? How would you make it possible to vote on those people?
- I would make a program that could vote for the top three funniest people in the office with the help of a class.
- I would 
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

Explanation for the code above:

- hhh

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

```commandline
from functools import reduce

numbers = [0, 5, 10, 20, 30, 40]


def sum_up(a, b): 
    return a + b


result_A = reduce(sum_up, numbers) 
print(result_A)
```

```commandline
from functools import reduce

print(reduce(lambda a, b: a + b, [0, 5, 10, 20, 30, 40])) 
```

#### 8. How does merge sort work?
- What is merge sort
- Example 

#### 9. Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is a use case?

An example of how to use a generator:

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

- hhh

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

- hhh

#### 10. Decorators - A page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator?
- A decorator is a function that accepts a function and returns a function i.e. the return value of a decorator function must be the function used to wrap the function to be decorated. 
   - Python will take the returned function and call it at decoration time, passing the function to be decorated.
   - As a decorator returns a function, a decorator does not have a specific return type. 

- list 2 good ideas of decorators and 2 bad??