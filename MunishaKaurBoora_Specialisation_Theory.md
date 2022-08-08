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

- list 2 good ideas of decorators and 2 bad??