"""
SEARCH IN MATRIX
--------

You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""


def search_in_matrix(matrix, target):
    for index, row in enumerate(matrix):
        if target in row:
            column = row.index(target)
            return [index, column]
    return [-1, -1]

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = 44

print(search_in_matrix(matrix, target))

"""
Explanation for the code above:
- Ive used the search_in_matrix function provided as a template for my code.
- Within the function, I've created a for loop and used the enumerate function with the for loop to print out each value of the list with a counter. 
   - In this case, the counter is the index number of each element in the list.
- I've then used an if statement to determine whether or not the target number is within each element, sublist, of the overall list stored within the matrix variable.  
   - If the target number is within a sublist, I obtain the index number on the target integer. This index number would be stored in the column variable.
   - Finally, the the row and column indices of the target integer would be returned.
- If the target number is not found, [-1, -1] would be returned.
"""

