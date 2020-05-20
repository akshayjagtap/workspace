'''
----------------------------------------
PYTHON SPECIFIC DATA STRUCTURES: STRINGS
----------------------------------------
Source:
https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=2

'''
new_line = '\n'
# There are two ways to escape quotes:
# 1. Using double quotes
string_1 = "This is Akshay's world"
print("String formatting using double quotes:\n{}{}".format(string_1, new_line))

# 2. Escaping the middle quote using \
string_2 = 'This is Akshay\'s world'
print("String formatting using escaping:\n{}{}".format(string_2, new_line))

# We can also print using tripple quotes example:
string_3 = \
    """Hello this is Akshay's world. I am
happy to start preparing for interviews.
"Keep going" in my motto"""

print("String using tripple quotes:\n{}{}".format(string_3, new_line))

# Strings are iterable meaning we can iterate over each character and fetch them by index
# the indexing starts from 0
# reverse indexing can be done starting from -1
string_4 = 'Hello World'

print("Slicing string '{}' using index 0: {}{}".format(
    string_4, string_4[0], new_line))

print("Slicing string '{}' using index 4: {}{}".format(
    string_4, string_4[4], new_line))

print("Slicing string '{}' using reverse index -1: {}{}".format(
    string_4,
    string_4[-1],
    new_line))

# We can grab a part of a string using indexes.
# Start and stop indexes are separated using colon :
# Python will include the start index in the output string but NOT the end index

print("Slicing string '{}' using start and end index: {}{}".format(
    string_4,
    string_4[0:5],
    new_line))

# When we don't specify the start index, python assumes it as 0 index
# so above example is similar to:

print("Slicing string '{}' using only end index: {}{}".format(
    string_4,
    string_4[:5],
    new_line))

# Similarly if end index is not provided, python assumes we want rest of the string
print("Slicing string '{}' using only start index: {}{}".format(
    string_4,
    string_4[6:],
    new_line))


'''
---------------------------
Built in methods for string
---------------------------
'''
# To find length of our string
print("Length of string '{}' using len() function: {}{}".format(
    string_4,
    len(string_4),
    new_line))

# To convert a string to all upper case
print("Converting '{}' to all upper case using .upper() function: {}{}".format(
    string_4,
    string_4.upper(),
    new_line))

# To convert a string to all lower case
print("Converting '{}' to all lower case using .lower() function: {}{}".format(
    string_4,
    string_4.lower(),
    new_line))

# To count a certain sub-string in a string
print("Counting sub-string 'Hello' in {} using .count() function: {}{}".format(
    string_4,
    string_4.count('Hello'),
    new_line))

# To count a certain character in a string
print("Counting character 'l' in {} using .count() function: {}{}".format(
    string_4,
    string_4.count('l'),
    new_line))

# To find the index of a sub-string or a character
print("Finding index of a sub-string 'World' from {} using .find() function: {}{}".format(
    string_4,
    string_4.find('Hello'),
    new_line))
# To find the index of a sub-string or a character
print("Finding index of a character 'W' from {} using .find() function: {}{}".format(
    string_4,
    string_4.find('W'),
    new_line))

# If .find(chr) does not find chr in the given string then it returns -1
pass

# Replacing one sub-string / character with another sub-string / character
string_5 = "Ye hai ICE ke sabse bade chamatkari purush."
string_6 = string_5.replace('chamatkari', 'balatkari')
print("Replaced '{}' to '{}' using .replace() method".format(string_5, string_6))
'''
IMPORTANT NOTE:
>>> message = "Hello World"
>>> message.replace('World', 'Universe')
>>> print(message)
Hello World

It did not print 'Hello Universe' because .replace() method DOES NOT making the replacement in-place. It actually
returns the newly formed string.
'''
