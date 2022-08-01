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
Explanation for code above:
- Ive used the function provided, generate_phrase, as a template for my code. 
   - I've kept the arguments 'characters' and 'phrase' provided. This is so that I can later test that the code produces the desired output by passing variables storing strings to the fucntion generate_phrase.
   
- Within the body of the function, generate_phrase, I've created a variable phrase_index and set it equal to 1. 
   - I've created this variable so that I can later use the index number of the string that I need to generate to slice the string.
   
- I've then created a for loop to iterate over the string stored in the variable passed to the function generate_phrase.
   - Within the for loop, I've created an if statement.
   - The if statement is used to help remove a character from the string that I need to generate and the string of available characters - provided that the charcater exists in both strings.
   - Within the if statement, I've created a variable, index, to help figure out the index number of a particular character within the the string of available characters (this is the chack if a character exists in both the string that I need to generate and the string of available characters).
   - Then, using the index number obtained, I slice both the string of available characters and the string that I need to generate, removibg the common chacrter from both strings.
   - I've removed 1 from the value stored in phrase_index so that, overall, the index number of the the string that I need to generate remains the same. I do this because I later add one to the value stored in phrase_index to move to the next index number but i wouldnt need to move to the next index number if a chacrter is removed from a string.
   - In the end, if all characters from the string that I need to generate exist in the string of available characters, I'd be left with an empyty string as the string that I need to generate. When tested, this string would return True as an output, thereby confirming that the characters in the string that I need to generate exist in the string of available characters. 


- Outside of the if statement, I've added 1 to the value stored in phrase_index so that the index number of the the string that I need to generate increases by 1.
- Finally, I return the output of 'phrase in characters'. 
   - The output would be True if the charcaters of the string that I need to generate exist in the string of available characters.
   - The output would be False if the charcaters of the string that I need to generate do not exist in the string of available characters.  
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

