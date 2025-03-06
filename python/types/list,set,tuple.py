# collection = single "variable" used to store multiple values

"""
# List = [] ordered and changable. Duplicates ok
The list can be represented by [ ]
Example: [1, 2, 3, 4, 5]


# Tuple = () ordered and unchangeable. Duplicates ok. FASTER 
A tuple can be represented by  ( )
Example: (1, 2, 3, 4, 5)


# Set = {} unordered and immutable(not changing, or unable to be changed), but Add/Remove ok. No duplicates
The set can be represented by { }
Example: {1, 2, 3, 4, 5}

# Dictonary = { Key : Value } ordered
The dictionary can be represented by { }
Example: {1: “a”, 2: “b”, 3: “c”, 4: “d”, 5: “e”}



# Lists:
Syntax: []
Ordered: Yes (Maintains the insertion order)
Mutable: Yes (Elements can be changed)
Duplicates: Yes (Allows duplicate elements)
Example: [1, 2, 3, 4]


# Tuples:
Syntax: ()
Ordered: Yes (Maintains the insertion order)
Mutable: No (Elements cannot be changed once assigned)
Duplicates: Yes (Allows duplicate elements)
Example: (1, 2, 3, 4)


# Sets:
Syntax: {} or set()
Ordered: No (No guarantee of order in Python versions before 3.7)
Mutable: Yes (Elements can be added or removed)
Duplicates: No (Does not allow duplicate elements)
Example: {1, 2, 3, 4}


# Dictionaries:
Syntax: {key: value}
Ordered: Yes (Maintains the insertion order starting from Python 3.7)
Mutable: Yes (Keys and values can be changed)
Duplicates: No (Keys must be unique, but values can be duplicated)
Example: {'a': 1, 'b': 2, 'c': 3}

"""
 


"      0, 1, 2, 3, 4    "
arr = [9, 8, 7, 6, 5]
# arr.append(4)
# arr.pop()
print(arr)

print(arr[-1])
print(arr[::-1]) # [ Start : Stop : Step ]

data = [23, 45, 12, 67, 34]
data.append(89)  # Add an item
data.remove(45)  # Remove an item
print(data)



sett = {9, 8, 6, 5, 7}
sett_alphabet = {"q", "A", "e", "c", "p"}
print(sett_alphabet)

# name = input("Enter yout name: ")
# print(name[-1])


datas = {
    'id': 1,
    'name': 'Babin',
    'email': 'babin@gmail.com',
    'age': 20
}
print(datas)
print(datas("name"))