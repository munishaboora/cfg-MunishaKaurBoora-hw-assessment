"""
Question 1 (20 points)

1.
A program is a set of instructions provided to the computer for it to perform. These instructions process input, manipulate data, and output a result.
For example, we have Microsoft Word which is a word processing program that allows users to create and write documents.

2.
A process is a program whilst it is in execution, in other words, a set of instructions being processed by a computer processor in the present time.

3.
Caches are used to temporarily store instructions and data that are likely to be reused by the central processing unit. This itself enables faster processing by the central processing unit.

4.
A thread is a small sequence of programmed instructions designed to be scheduled and executed by the central processing unit.
Multithreading enables multiple threads to be executed simultaneously. These multiple threads can perform different tasks in a single program.

5.
GIL stands for Global Interpreter Lock. GIL is a lock which allows only one thread at a time to hold control of the python interpreter. It works by allowing only one thread to be in a state of execution at any point in time.

6.
Concurrency is when an application is making progress on more than one task at the same time. In other words, when tasks overlap in execution.
Parallelism is when an application splits up tasks into smaller subtasks which can be processed in parallel.
Differences:
   - Concurrency can be achieved using a single processing unit whereas parallelism requires multiple processing units.
   - Concurrency involves running and managing multiple computations at the same time whereas parallelism involves running multiple computations simultaneously.
   - Concurrency increases the amount of work accomplished at a time whereas parallelism improves the throughput and computational speed of the system.

7.
DRY stands for 'don't repeat yourself'. The 'dont repeat yourself' principle aims to reduce the repetition of patterns and code duplication within one's work to avoid redundancy.
KISS stands for 'keep it simple stupid'. The 'keep it simple stupid' principle states that one should keep their code simple and avoid unnecessaruy complexity, resulting in code that is both easier to understand and maintain.
BDUF stands for 'big design up front'. The ‘Big Design Up Front’ principle states that one should spend more time designing an application before moving on to writing the first line of code for the application.

8.
In general, a garbage collector is a piece of software that automatically manages memory.
When it comes to python, garbage collection is performed automatically. Python deletes unwanted objects automatically to free up memory space.
Python's garbage collector runs during a program's execution and it is triggered when an objects reference count reaches zero.

9.
A deadlock is a condition which occurs when two or more transactions are waiting indefinitely for one another to give up locks.
A livelock is a condition which occurs when a request for an exclusive lock is continuously denied.
   - This is due to many overlapping shared locks continuously interfering each other.
   - The two or more programs repeatedly changing their state results in neither program making progress.

10.
Flask is a backend framework written in python. Flask is used to build web applications.
Flask is beneficial because it provides one with tools, libraries and technologies that allow one to build a web application.

"""


"""
Question 2 (8 points)
Some key difference between python 2 and python 3 are: the print function, the storage of strings, the division of integers, iteration and exceptions.
In python 2 print is considered a keyword, print "hello". In Python 3 print is considered a function, print("Hi").
In python 2 strings are stored as ASCII by default. In Python 3 strings are stored as UNICODE by default.
In python 2 when two integers are divided, an integer value is always returned. In Python 3 when two integers are divided, a floating-point value is always returned.
In python 2 the xrange() function is used for iterations. In Python 3, the range() function was introduced to perform iterations.
In python 2, exceptions are enclosed in notations. In Python 3, exceptions are enclosed in parentheses.
"""


"""
Question 3 (8 points)
Note: for this question I have assumed that I was required to return True or False as an output and that an individual would only pass a string to the function rather than, for instance, a list of multiple strings.
"""
def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word


print(is_palindrome('hannah'))
print(is_palindrome('bobby'))


"""
Question 4 (8 points)
For this question, I would typically create a separate file to write the code for the unit tests. Within the separate file, I would write the exact code I've written below. The test file would typically be in the same folder as the file containing the function to be tested.
For the is_palindrome() function, I have decided to perform two different unit tests:
   - I have performed one unit test where the word in the string passed to the function is not a palindrome to dertermine if the correct output of False is returned.
   - I have also performed one unit test where the word in the string passed to the function is a palindrome to determine if the correct output of True is returned.
"""

from unittest import TestCase, main
from MunishaKaurBoora_assessment_two import is_palindrome


class TestPalindrome(TestCase):
    def test_palindrome_word(self):
        expected = True
        result = is_palindrome(word='bob')
        self.assertEqual(expected, result)

    def test_not_palindrome_word(self):
        expected = False
        result = is_palindrome(word='joe')
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()

"""
Question 5 (8 points)
Agile teams take part in: requirement meetings, architecture and design meetings, test and feedback meetings, and development meetings.
Requirement meeting: the objective of a requirement meeting is to discuss the project's requirements with the main stakeholders of the project. The stakeholders of a project can be the projects owner, individuals using the software to be created, a subject matter expert, etc.
   - In this meeting of a project, the development team would be highly involved as they would need to take in the information from the meeting to determine what is actually required of them. 
   - In this meeting, the person requiring the project to be completed, the project owner, may not have the required skillset to design and build the project themselves, making this stage crucial to get their requirements across clearly to the developers.
Architecture and design meeting: in this meeting developers begin to design the software.
   - Within an agile environment, one may quickly design and create something to use as a starting point for future prototypes.
   - Within this meeting, developers may use various tools such as miro to come up with potential project designs. Miro can be used to design mobile apps or even to flesh out ideas as a team.
   - One may also decide on the file structure of the project, for instance splitting it up into smaller managable components (typically one function per file used).
Test and feedback meeting:   
   - This stage involves ensuring that the software works as intended and if it does not, it may result in reverting to previous stages within the software development life cyle. 
   - One may perform unit testing on for instance functions within the code, regression testing to determine if other aspects of the project have been affected by changing one aspect of the project's code, or even user acceptance testing where users acually use the software to test it.

"""

"""
Question 6 (8 points)
try: the code in the try block is run and if the code executes as intended, the else statement is executed. If the code doesnt execute as intended then the except block is executed.
except: the code in the except block is executed is there is an exception i.e. if the code in the try block doesnt execute as intended.
else: the code in the else block is executed if there is no exception.
finally: the code in the finally block is executed no matter what - exception or no exception. 

The try/except/else/finally block is used to deal with potential errors in one's code. For instance when trying to withdraw money from a cashpoint without having sufficient funds. In such a situation, one would use exception handling to throw an error when one attempts to withdraw more money than is in one's account.
"""
# Example for question 6:
def is_palindrome(word):
    try:
        reversed_word = word[::-1]
        return word == reversed_word
    except ValueError:
        ("Invalid word format entered")
    finally:
        print("Thank you for using this palindrome checker.")

"""
Question 7 (8 points)
In order to connect a python program with a database such as MySQL, we would firstly require the username and password to even be able to access the database - this is typically placed in the configuration file.
Python cannot connect directly to a database, in order to do this it needs something called a database engine - also known as a driver or connector. We would have to install the connector.
Once we are able to connect to a database, we are returned something called a cursor. We are able to pass this cursor SQL syntax that it will execute.
In order to fetch /insert data into a database from a python program, we must also have defined the routes we are to use. Within these routes, we can define functions that perform certain actions such as adding or removing data from SQL.
We can test the successful insertion of data into a database using alternative software such as postman. This is because such actions would require a PUT request which is not visible in the browser using one's local host url.
"""




"""
Question 8 (10 points)

SELECT 
    a.author_name AS 'Author Name',
    SUM(b.sold_copies) AS 'Copies Sold'
FROM
    Authors a
        LEFT JOIN
    Books b ON a.book_name = b.book_name
GROUP BY a.author_name
ORDER BY 2 DESC
LIMIT 3;
"""


"""
Question 9 (22 Points)
"""
def sum_of_list(numbers_list, target_sum):
    final_list = []

    for index, number in enumerate(numbers_list):
        required_number = target_sum - number
        first_half_of_list = numbers_list[:index]
        second_half_of_list = numbers_list[index + 1:]
        concatenated_list = first_half_of_list + second_half_of_list
        if required_number in concatenated_list:
            final_list.extend((number, required_number))
            break

    return final_list


print(sum_of_list([2, 2, 3], 5))
print(sum_of_list([2, 2, 3, 23, 9, 11], 20))
print(sum_of_list([2, 2, 3], 10))


"""
Explanation for the function above:
- I have created a function called sum_of_list and passed it the parameters numbers_list and target_sum to act as placeholders for a list and a target sum respectively.
- Within the body of the function, I've created a variable final_list which stores an empty list to start off with. This list will store elements of the original list that add together to give the target sum - provided that such elements exist in the list. 
- I have then created a for loop to iterate through a list passed to the function. I've used a for loop in conjunction with the the enumerate() function to return the index number of each element in the original list.
   - Within the for loop, I've created a variable called required_number, representing the number that would need to be added to an element in the original list to reach the target sum.
   - I've also created three additional variables first_half_of_list, second_half_of_list and concatenated_list. These variables will be used form a list consisting of all elements of the original list excluding the present value in the for loop.
   - I've used an if statement to determine whether or not the required number is in the new list, concatenated_list. 
      - If the value is present in the new list, both the required number and present value in the loop are added to the empty list stored in final_list. After this, the for loop is exited and the list stored in final_list is returned.
      - If the value is not present in the new list, the loop continues to iterate over the remaining elements in the original list until either two values adding to give the target sum are found or until the loop ends.
"""








