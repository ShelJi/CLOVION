from icecream import ic

# String manipulation refers to the process of modifying, parsing, 
# and analyzing strings in programming. Strings are sequences of 
# characters, and manipulating them is a common task in software 
# development. String manipulation involves a variety of operations, 
# such as concatenation, slicing, trimming, searching, replacing, and more.

# Common String Manipulation Operations

# Concatenation: Combining two or more strings into one.

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # "Hello World"

# Slicing: Extracting a substring from a string.

str = "Hello World"
substring = str[0:5]  # "Hello"

# Trimming: Removing whitespace or other characters from the beginning or end of a string.

str = "   Hello World   "
trimmed_str = str.strip()  # "Hello World"

# Searching: Finding the position of a substring within a string.

str = "Hello World"
position = str.find("World")  # 6

# Replacing: Substituting a part of the string with another string.

str = "Hello World"
new_str = str.replace("World", "Python")  # "Hello Python"

# Splitting: Dividing a string into a list of substrings based on a delimiter.

str = "apple,banana,cherry"
fruits = str.split(",")  # ["apple", "banana", "cherry"]

# Joining: Combining a list of strings into a single string with a delimiter.

fruits = ["apple", "banana", "cherry"]
str = ",".join(fruits)  # "apple,banana,cherry"

# Changing Case: Converting strings to uppercase or lowercase.

str = "Hello World"
upper_str = str.upper()  # "HELLO WORLD"
lower_str = str.lower()  # "hello world"

# Reversing: Reversing the order of characters in a string.

str = "Hello World"
reversed_str = str[::-1]  # "dlroW olleH"

# Examples in Python
# Here are a few examples of string manipulation in Python:

# Example string
text = "   Hello, OpenAI! Welcome to the world of AI.   "

# Removing leading and trailing whitespace
trimmed_text = text.strip()

# Converting to uppercase
upper_text = trimmed_text.upper()

# Replacing substring
replaced_text = upper_text.replace("OPENAI", "GPT-4")

# Finding a substring
position = replaced_text.find("WORLD")

# Slicing
substring = replaced_text[7:14]

# Splitting into a list
words = replaced_text.split()

# Joining a list into a string
joined_text = " ".join(words)

# Displaying results
print("Trimmed Text:", trimmed_text)
print("Upper Text:", upper_text)
print("Replaced Text:", replaced_text)
print("Position of 'WORLD':", position)
print("Substring:", substring)
print("Words List:", words)
print("Joined Text:", joined_text)

# String manipulation is essential for tasks like data processing,
#  user input validation, text analysis, and many other areas in programming.