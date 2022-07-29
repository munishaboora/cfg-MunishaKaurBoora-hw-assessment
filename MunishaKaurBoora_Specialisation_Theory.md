#### 1. How does Object Oriented Programming differ from Process Oriented Programming?

- Object Oriented Programming is ...
   - Describe OOP
   - Example of OOP x 2
   - Explain example 
- Process Oriented Programming is ...

#### 2. What's polymorphism in OOP?
- Describe polymorphism and provide 2 examples ...


#### 3. What's inheritance in OOP?
- Describe inheritance and provide 2 examples ...

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



#### 5. What's the software development cycle?


#### 6. What's the difference between agile and waterfall?


#### 7. What is a reduced function used for?


#### 8. How does merge sort work?


#### 9. Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is a use case?
**An example of how to use a generator:**




#### 10. Decorators - A page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator?

