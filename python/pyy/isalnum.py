# The isalnum() method is 
# a string method that checks whether all the 
# characters in a string are alphanumeric. Here’s 
# a breakdown of what it does:

# Definition: isalnum() returns True if all 
# characters in the string are alphanumeric 
# (letters or numbers), and there is at least one character.
# If the string is empty or contains non-alphanumeric 
# characters, it returns False.

# Usage: It is often used in conjunction with 
# other string methods or in conditions to filter 
# or validate strings based on their alphanumeric content.

# Example:
s1 = "Hello123"
s2 = "Hello 123"  # contains a space
s3 = "123"        # only digits
s4 = "Hello"      # only letters
s5 = ""           # empty string

print(s1.isalnum())  # True
print(s2.isalnum())  # False
print(s3.isalnum())  # True
print(s4.isalnum())  # True
print(s5.isalnum())  # False

# Explanation of Examples:
# s1.isalnum() returns True because all characters 
# ('H', 'e', 'l', 'l', 'o', '1', '2', '3') are alphanumeric.
# s2.isalnum() returns False because it contains a space (' ').
# s3.isalnum() returns True because all characters 
# ('1', '2', '3') are digits.
# s4.isalnum() returns True because all characters 
# ('H', 'e', 'l', 'l', 'o') are letters.
# s5.isalnum() returns False because it is an empty string.
# Use Cases:
# Input Validation: Checking user input to ensure it 
# only contains letters and numbers.
# String Processing: Filtering out non-alphanumeric 
# characters from a string before further manipulation.
# Palindrome Check: Cleaning a string for palindromes 
# by removing non-alphanumeric characters using isalnum().
# In summary, char.isalnum() is used to determine if a 
# character (char) is alphanumeric (a letter or a digit). 
# It helps in handling strings based on their content, 
# particularly in scenarios where alphanumeric characters are expected or required.