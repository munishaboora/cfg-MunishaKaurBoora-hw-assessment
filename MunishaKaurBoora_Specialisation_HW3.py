
def generate_phrase(characters, phrase):




# def generate_phrase(characters, phrase):
#     sorted_phrase = sorted(phrase)
#     phrase_index = 1
#     for letter in phrase:
#
#         if phrase[:phrase_index] in characters:
#             index = characters.find(phrase[:phrase_index])
#             characters = characters[:index] + characters[index+1:]
#
#             phrase = phrase[:phrase_index-1] + phrase[phrase_index:]
#             print(phrase)
#             phrase_index -= 1
#         continue
#         phrase_index += 1
#
#
#         return phrase in characters




###################################################

# Test case 1 -- False

# characters = "odeC stFir slrG"
# phrase = "Code First Girls"
#
# print(generate_phrase(characters, phrase))

###################################################

# Test case 2 -- False

# characters = "A"
# phrase = "a"
#
# print(generate_phrase(characters, phrase))

###################################################

# Test case 3 -- True

# characters = "odeC stFir slrG"
# phrase = ""
#
# print(generate_phrase(characters, phrase))

###################################################

# Test case 4 -- True

characters = "aheaollabbhb"
phrase = "hello"

print(generate_phrase(characters, phrase))
