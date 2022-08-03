def generate_phrase(characters, phrase):
    phrase_index = 1

    for letter in phrase:

        if letter in characters:
            index = characters.find(letter)
            characters = characters[:index] + characters[index+1:]
            phrase = phrase[:phrase_index-1] + phrase[phrase_index:]
            phrase_index -= 1

        phrase_index += 1

    return phrase in characters
"""
Explanation for the code above:
- Ive used the function provided, generate_phrase, as a template for my code. 
   - I've kept the arguments 'characters' and 'phrase' provided. This is so that I can later test that the code above produces the desired output by passing variables that store strings to the fucntion generate_phrase.
   
- Within the body of the function, generate_phrase, I've created a variable phrase_index and set it equal to 1. 
   - I've created this variable so that I can later use index numbers to slice the string that I need to generate.
   
- I've then created a for loop to iterate over the string stored in the variable passed to the function generate_phrase.
   - Within the for loop, I've created an if statement.
      - The if statement is used to help remove a character from the string that I need to generate and the string of available characters - provided that the charcater exists in both strings.
      - Within the if statement, I've created a variable, index, to help figure out the index number of a particular character within the the string of available characters (this is to check if a character exists in both the string that I need to generate and the string of available characters).
      - Then, using the index number obtained, I slice both the string of available characters and the string that I need to generate, removing the common chacrter from both strings.
      - I've removed 1 from the value stored in phrase_index so that, overall, the index number of the the string that I need to generate remains the same. I do this because I later add one to the value stored in phrase_index to move to the next index number but I wouldnt need to move to the next index number if a character is removed from a string.
   - In the end, if all characters from the string that I need to generate exist in the string of available characters, I'd be left with an empyty string as the string that I need to generate. 
      - When tested, this string would return True as an output, thereby confirming that the characters in the string that I need to generate exist in the string of available characters. 


- Outside of the if statement, I've added 1 to the value stored in phrase_index so that the index number of the the string that I need to generate increases by 1.
- Finally, I return the output of 'phrase in characters'. 
   - The output would return True if the characters of the string that I need to generate exist in the string of available characters.
   - The output would return False if the characters of the string that I need to generate do not exist in the string of available characters.  
"""

"""
 - I have haven't refactored the generate_phrase function as I felt that I did not need to.
 - I've made sure to include a return statement in the generate_phrase function so that I can test the code.
 - Please refer to the unit_tests.py file for the unit tests corresponding to the generate_phrase function.
"""

###################################################
# Test case 1 -- False

characters = "odeC stFir slrG"
phrase = "Code First Girls"

print(generate_phrase(characters, phrase))
###################################################

###################################################
# Test case 2 -- False

characters = "A"
phrase = "a"

print(generate_phrase(characters, phrase))
###################################################

###################################################
# Test case 3 -- True

characters = "odeC stFir slrG"
phrase = ""

print(generate_phrase(characters, phrase))
###################################################

###################################################
# Test case 4 -- True

characters = "aheaollabbhb"
phrase = "hello"

print(generate_phrase(characters, phrase))
###################################################