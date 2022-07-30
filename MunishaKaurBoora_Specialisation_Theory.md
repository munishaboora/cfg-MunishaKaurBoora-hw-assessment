#### 1. How does Object Oriented Programming differ from Process Oriented Programming?

- Object Oriented Programming is ...
   - Describe OOP
   - Example of OOP x 2
   - Explain example 
- Process Oriented Programming is ...
   - Describe OOP
   - Example of OOP x 2
   - Explain example 

- The key differences between Object Oriented Programming and Process Oriented Programming are:
   - print
      - Object Oriented Programming: .... 
      - Process Oriented Programming: ....
   - print
      - Object Oriented Programming: .... 
      - Process Oriented Programming: ....
   - print
      - Object Oriented Programming: .... 
      - Process Oriented Programming: ....
   - print
      - Object Oriented Programming: .... 
      - Process Oriented Programming: ....
   - print
      - Object Oriented Programming: .... 
      - Process Oriented Programming: ....

#### 2. What's polymorphism in OOP?
- Describe polymorphism and provide 2 examples ...
- Explain the exmaples
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


#### 6. What's the difference between agile and waterfall?


#### 7. What is a reduced function used for?


#### 8. How does merge sort work?


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

