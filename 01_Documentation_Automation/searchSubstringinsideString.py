__doc__ = "Search SubString inside String"
__author__ = "Abhishek Shinde | EXD-AS"
__contact__ = "arabhishek1091@gmail.com"

substring = ["Hello", "great", "Python", "Hello Alex"]
string = ["Hello, how are you?", "Hello in life where do you stand Alex?", "I am doing great.", "Python is awesome!"]

# LOGIC 1 - Search substring inside string
# Note: The values are stored in dictionary
# Python has Limitation on maximum size of dictionary keys hence wierd output when search logic is implemented
# Look at LOGIC 2 and the explaination below
stringlist_dict = {}

for strng in string:
    found_substrings = []
    for substr in substring:
        if substr.lower() in strng.lower():
            found_substrings.append(substr)
    stringlist_dict[strng] = found_substrings

print(stringlist_dict)

# LOGIC 2 - Search substring inside string
# Note: The values are stored in Tuples
stringlist_tuples = []

for strng in string:
    found_substrings = []
    for substr in substring:
        if substr.lower() in strng.lower():
            found_substrings.append(substr)
    stringlist_tuples.append((strng, found_substrings))

print(stringlist_tuples)



#LOGIC 3
def search_substrings(string_list, substrings):
    found_strings = {}

    for string in string_list:
        for substring in substrings:
            if all(sub in string for sub in substring.split()):
                found_strings[string] = substring
                break

    return found_strings

found_strings = search_substrings(string, substring)

"""
EXPLANATION WHY TUPLES 
**********************

In Python, the limit on the maximum size of dictionary keys is determined by the available system memory. 
Since dictionary keys are stored in memory, the maximum size of a dictionary key will depend on the available 
memory in the system.
Python dictionaries use hash-based lookup, where the keys are hashed to determine their storage location in memory. 
The hashing algorithm used by Python ensures efficient and fast access to dictionary elements. However, the size of
the dictionary key itself is subject to memory limitations.
In practical terms, the maximum size of a dictionary key is typically constrained by the available memory and the 
maximum addressable memory space of the system. If you attempt to use very large objects as keys or have a large 
number of keys, you may encounter memory-related issues.
It's worth noting that Python's dictionaries are highly optimized for most use cases and are generally efficient and 
performant. However, if you find that the size or number of keys is causing performance or memory issues, you may 
need to consider alternative approaches or data structures to handle your specific requirements.
"""