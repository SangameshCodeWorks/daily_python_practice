# ==============================================================================
# Module: ALLdatatypesPractice.py
# Topic: Comprehensive Practice of Python Data Types & Their Core Built-in Methods
# Covering: Lists, Sets, Dictionaries, and Strings
# ==============================================================================

# ==============================================================================
# SECTION 1: LIST CREATION AND METHODS
# ==============================================================================
print("#*********list creation and its methods*******")

# ------------------------------------------------------------------------------
# List Initialization
# • What is it for: Creating ordered, mutable sequences that support mixed types and duplicate values.
# • What it does:
#   - l1 contains integers, string ('raj'), float (35.2), boolean (True), complex (33j), and duplicate 20.
#   - l2 contains integers with duplicates.
# • Where it is used: Storing heterogeneous collections, batch records, queue buffers.
# ------------------------------------------------------------------------------
l1 = [20, 35, "raj", 35.2, True, 33j, 20]
l2 = [35, 36, 20, 466, 20]

# ------------------------------------------------------------------------------
# append(object) Method
# • What is it for: Adding a single element to the very end of the list.
# • What it does: Appends integer 100 as the final element of l1.
# • Where it is used: Adding a newly arrived item to an inventory or list of notifications.
# ------------------------------------------------------------------------------
    #append(object) Method add the key at the end of the list
l1.append(100)
print(l1)

# ------------------------------------------------------------------------------
# extend(iterable) Method
# • What is it for: Appending all elements of another collection into the current list in-place.
# • What it does: Unpacks elements of l2 and appends each one to l1.
# • Where it is used: Merging pagination batches from API requests into a main list.
# ------------------------------------------------------------------------------
    #extend it will joins the 2 list
l1.extend(l2)
print(l1)

# ------------------------------------------------------------------------------
# insert(index, object) Method
# • What is it for: Inserting an element at an exact index position.
# • What it does: Inserts value 10 at index 1, shifting subsequent elements to the right.
# • Where it is used: Adding a VIP customer to the front or specific priority slot of a line.
# ------------------------------------------------------------------------------
    #insert(i,object) it add the new value to given index
l1.insert(1, 10)
print(l1)

# ------------------------------------------------------------------------------
# pop() Method
# • What is it for: Removing and returning the last element from the list.
# • What it does: Removes the final element of l1 and shortens the list length by 1.
# • Where it is used: Implementing undo actions, popping items from a processing stack.
# ------------------------------------------------------------------------------
    #pop it will delete the last element or value
l1.pop()
print(l1)

# ------------------------------------------------------------------------------
# remove(object) Method
# • What is it for: Deleting the first occurrence of a specific value.
# • What it does: Searches for 35 and removes the first instance found in l1.
# • Where it is used: Deleting a specific product ID from a user's wishlist.
# ------------------------------------------------------------------------------
    #remove(object) method it removes the particular object
l1.remove(35)
print(l1)

# ------------------------------------------------------------------------------
# count(object) Method
# • What is it for: Counting how many times a given element appears in the list.
# • What it does: Counts occurrences of 20 in l1.
# • Where it is used: Tallying poll results, tracking frequency of errors in a log list.
# ------------------------------------------------------------------------------
    #count(object) it will count how many time the object is repeted
print(l1.count(20))

# ------------------------------------------------------------------------------
# index(object) Method
# • What is it for: Finding the zero-based index of the first occurrence of an element.
# • What it does: Finds and returns the first index position where 20 appears.
# • Where it is used: Finding where an item is located before replacing or inspecting adjacent items.
# ------------------------------------------------------------------------------
    #index(object) it will returns first occaring the index of the given object
ind = l1.index(20)
print(ind)

# ------------------------------------------------------------------------------
# reverse() Method
# • What is it for: Reversing the order of items in the list in-place.
# • What it does: Flips the entire list order without creating a new copy.
# • Where it is used: Showing transaction history from newest to oldest.
# ------------------------------------------------------------------------------
    #reverse it will reverse the whole list
l1.reverse()
print(l1)

# ------------------------------------------------------------------------------
# clear() Method
# • What is it for: Removing all elements from the list, making it empty [].
# • What it does: Clears all contents from l1 while keeping the list object reference intact.
# • Where it is used: Resetting a game board, flushing temporary data queues.
# ------------------------------------------------------------------------------
    #clear it will delete all the elements from the list
l1.clear()
print(l1)
print("************************************************************************************")


# ==============================================================================
# SECTION 2: SETS CREATION AND METHODS
# ==============================================================================
print("#*********sets creation and its methods*******")

# ------------------------------------------------------------------------------
# Set Initialization
# • What is it for: Storing unordered collections of unique elements.
# • What it does: Initializes s1 and s2 with integer sets, automatically discarding any duplicate entries.
# • Where it is used: High-speed O(1) membership testing and eliminating duplicates.
# ------------------------------------------------------------------------------
s1 = {4, 7, 9, 3, 8, 2, 12, 11}
s2 = {12, 15, 11, 19, 10, 9, 3}

# ------------------------------------------------------------------------------
# add(object) Method
# • What is it for: Adding a single unique element to the set.
# • What it does: Inserts 90 into s1. If 90 is already present, does nothing.
# • Where it is used: Tracking visited web URLs in a web crawler to prevent infinite loops.
# ------------------------------------------------------------------------------
    #add(object) method it will add the object at the any where
s1.add(90)
print(s1)

# ------------------------------------------------------------------------------
# update(iterable) Method
# • What is it for: Adding multiple elements from another collection into the set.
# • What it does: Merges all items from s2 into s1, maintaining uniqueness.
# • Where it is used: Aggregating unique user IDs across multiple marketing campaigns.
# ------------------------------------------------------------------------------
    #update combines both the set1 and set2
s1.update(s2)
print(s1)

# ------------------------------------------------------------------------------
# pop() Method on Sets
# • What is it for: Removing and returning an arbitrary element from the set.
# • What it does: Removes whatever element is currently first in hash table order.
# • Where it is used: Consuming tasks from a non-prioritized worker pool.
# ------------------------------------------------------------------------------
    #pop it removes the any one element from the set
val = s1.pop()
print(s1, val)

# ------------------------------------------------------------------------------
# remove(object) vs discard(object)
# • What is it for: Deleting a specific element from the set.
# • What it does:
#   - remove(90): Deletes 90. If item is missing (like 99), raises KeyError.
#   - discard(99): Deletes 99 if present; if absent, does nothing safely without error.
# • Where it is used:
#   Use remove() when missing items represent data corruption; use discard() for safe cleanup.
# ------------------------------------------------------------------------------
    # remove(object) it remove the particular object from the set
s1.remove(90)
print(s1)
'''s1.remove(99)
        print(s1)
        Traceback (most recent call last):
          File "F:/CodePlayground/Python Workspace/ALLdatatypesPractice.py", line 49, in <module>
            s1.remove(99)
                KeyError: 99'''
    #discard(object) as same as remove but it wont return the error iff the given element is not present in set
s1.discard(99)
print(s1)

# ------------------------------------------------------------------------------
# issubset() and issuperset() Methods
# • What is it for: Testing set containment relationships.
# • What it does:
#   - s1.issubset(s2): Checks if every element of s1 is in s2.
#   - s1.issuperset(s2): Checks if s1 contains all elements of s2.
# • Where it is used: Verifying if a user has all mandatory permissions required for a role.
# ------------------------------------------------------------------------------
    #issubset check it the subset of set 2
val2 = s1.issubset(s2)
print(val2)
    #issuperset check s1 is super set of set2
val3 = s1.issuperset(s2)
print(val2)

# ------------------------------------------------------------------------------
# isdisjoint() Method
# • What is it for: Checking if two sets have NO common elements.
# • What it does: Returns True if intersection is empty; False if there is any shared element.
# • Where it is used: Detecting scheduling conflicts between calendar appointments.
# ------------------------------------------------------------------------------
    #isdisjoint it checks is the any comman element is there means returns false
val4 = s1.isdisjoint(s2)
print(val4)

# ------------------------------------------------------------------------------
# union() Method
# • What is it for: Combining all elements of both sets without duplicates.
# • What it does: Produces a new set with every item from s1 and s2.
# • Where it is used: Combining email subscriber lists from two different newsletters.
# ------------------------------------------------------------------------------
    #union it add the both the set and duplicate elements only one time
val5 = s1.union(s2)
print(val5)

# ------------------------------------------------------------------------------
# intersection() Method
# • What is it for: Finding elements that exist in BOTH sets.
# • What it does: Returns a set containing only items present in both s3 and s4 -> {55, 66}.
# • Where it is used: Finding mutual contacts on social networks or common skills in job matching.
# ------------------------------------------------------------------------------
s3 = {33, 44, 55, 66}
s4 = {55, 66, 77, 88}
    #intersection it will return only comman elements
val6 = s3.intersection(s4)
print(val6)

# ------------------------------------------------------------------------------
# difference() Method
# • What is it for: Finding elements present in the first set but NOT in the second set.
# • What it does: Returns items in s3 that are absent from s4 -> {33, 44}.
# • Where it is used: Finding unsubscribed users or pending tasks not yet completed.
# ------------------------------------------------------------------------------
s3 = {33, 44, 55, 66}
s4 = {55, 66, 77, 88}
    #difference it will return the elements of set1 without comman elements is present in both side
val8 = s3.difference(s4)
print(val8)

# ------------------------------------------------------------------------------
# symmetric_difference() Method
# • What is it for: Finding elements that are in either set, but NOT in both (disjunctive union).
# • What it does: Returns items unique to s3 or unique to s4 -> {33, 44, 77, 88}.
# • Where it is used: Identifying discrepancies when syncing records between two databases.
# ------------------------------------------------------------------------------
    #symmetric_diffrence it will return both set elements without comman elements
val9 = s3.symmetric_difference(s4)
print(s4)

print("************************************************************************************")


# ==============================================================================
# SECTION 3: DICTIONARY CREATION AND METHODS
# ==============================================================================
print("#*********Dictionary creation and its methods*******")

# ------------------------------------------------------------------------------
# Dictionary Initialization
# • What is it for: Storing structured data as associative key-value pairs.
# • What it does: Creates profiles d1 and d2 with name, age, city, experience, and course.
# • Where it is used: Representing database records, user profiles, API JSON objects.
# ------------------------------------------------------------------------------
d1 = {
    'name1': "sangamesh",
    'age1': 22,
    'city1': "bangalore",
    'exp1': 2.5,
    'course1': "python fullstack"
}

d2 = {
    'name': 'vishwa',
    'age': 23,
    'city': 'gulbarga',
    'exp': 3.2,
    'course': 'data science'
}

print("                                     .                                   ")

# ------------------------------------------------------------------------------
# setdefault(key, default) Method
# • What is it for: Setting a key with a default value only if it does not already exist.
# • What it does: Adds 'ispass': True to d1 because 'ispass' was not present.
# • Where it is used: Initializing counters, building nested dictionaries without checking 'if key in dict'.
# ------------------------------------------------------------------------------
    #setdefault adding the item to the dictionary
d1.setdefault('ispass', True)
print(d1)

# ------------------------------------------------------------------------------
# update(other_dict) Method
# • What is it for: Merging key-value pairs from one dictionary into another.
# • What it does: Copies all key-value pairs from d2 into d1.
# • Where it is used: Overwriting default application settings with user-customized preferences.
# ------------------------------------------------------------------------------
    #update method it combines the both dictionary
d1.update(d2)
print(d1)

# ------------------------------------------------------------------------------
# get(key, default=None) Method
# • What is it for: Safely retrieving a value by its key without raising KeyError if missing.
# • What it does: Retrieves value for 'course' ('data science').
# • Where it is used: Querying optional fields in web requests and configurations.
# ------------------------------------------------------------------------------
    #get(key) method it access the particular key and value
value = d1.get("course")
print(value)

# ------------------------------------------------------------------------------
# popitem() Method
# • What is it for: Removing and returning the last inserted key-value pair.
# • What it does: Removes the last item ('course': 'data science') as a tuple.
# • Where it is used: Unwinding state changes, cache eviction.
# ------------------------------------------------------------------------------
    #popitem it only delete the last item  from the dictionary
d1.popitem()
print(d1)

# ------------------------------------------------------------------------------
# pop(key) Method
# • What is it for: Removing a specified key and returning its value.
# • What it does: Deletes key "age" from d1 and returns its value.
# • Where it is used: Removing sensitive fields (like password or token) before returning user data to client.
# ------------------------------------------------------------------------------
    # pop(key) it remove the particular item from the dictinary
d1.pop("age")
print(d1)

print("                                     .                                   ")

# ------------------------------------------------------------------------------
# keys(), values(), and items() View Methods
# • What is it for: Inspecting keys, values, and pair tuples in the dictionary.
# • What it does:
#   - keys(): Returns dict_keys view of all keys in d1.
#   - values(): Returns dict_values view of all values in d1.
#   - items(): Returns dict_items view of (key, value) tuples.
# • Where it is used: Looping through database records, generating table headers and rows.
# ------------------------------------------------------------------------------
    #keys gives only keys from the dictionary in the form of list
val11 = d1.keys()
print(val11)

print("                                     .                                   ")

    #values gives only values from the dictionary in the form of list
val12 = d1.values()
print(val12)

print("                                     .                                   ")

    #items it returns all the items in the form of tuples inside the list
val13 = d1.items()
print(val13)

print("                                     .                                   ")

# ------------------------------------------------------------------------------
# clear() Method on Dictionary
# • What is it for: Deleting all key-value pairs from the dictionary.
# • What it does: Empties d2 completely, leaving {}.
# • Where it is used: Clearing active session data on user logout.
# ------------------------------------------------------------------------------
    #clear
d2.clear()
print(d2)

print("************************************************************************************")


# ==============================================================================
# SECTION 4: STRINGS CREATION AND METHODS
# ==============================================================================
print("#*********STRINGS creation and its methods*******")

# Initialize sample strings with mixed case and whitespace
st1 = "sanGamesh jaiNapur mail @123"
st2 = "sanGamesh jaiNapur mail @123"
st3 = "  sanGamesh jaiNapur mail @123  "

# ------------------------------------------------------------------------------
# capitalize() Method
# • What is it for: Capitalizing only the first character and lowercasing the rest.
# • What it does: Converts first character to 'S', rest to lowercase.
# • Where it is used: Sentence capitalization in text formatting.
# ------------------------------------------------------------------------------
    #capitalize it make the first latter of the word is capital letter
st11 = st1.capitalize()
print("str11 >>>>>>", st11)

# ------------------------------------------------------------------------------
# title() Method
# • What is it for: Capitalizing the first character of each word.
# • What it does: Converts "sanGamesh jaiNapur..." to "Sangamesh Jainapur...".
# • Where it is used: Formatting names, book titles, headers.
# ------------------------------------------------------------------------------
    #title it makes the every word first latter in capital letter of the sentance
st1 = st1.title()
print(st1)

# ------------------------------------------------------------------------------
# upper() and isupper() Methods
# • What is it for: Uppercasing all characters and validating uppercase status.
# • What it does: upper() converts all letters to uppercase; isupper() checks if all letters are uppercase (returns True/False).
# • Where it is used: Normalizing country/state codes ("USA", "KA"), uppercase validation.
# ------------------------------------------------------------------------------
    #upper make all the letter in upper case
st1 = st1.upper()
print(st1)

    #isupper make all the letter in upper case or not it will check TRUE/FALSE
st1 = st1.isupper()
print(st1)

# ------------------------------------------------------------------------------
# lower() and islower() Methods
# • What is it for: Lowercasing all characters and validating lowercase status.
# • What it does: lower() turns all characters lowercase; islower() checks if all letters are lowercase.
# • Where it is used: Email address normalization for database storage and search.
# ------------------------------------------------------------------------------
    #lower make all the letter in lower case
st2 = st2.lower()
print(st2)

    #islower make all the letter in lower case or not it will check TRUE/FALSE
st2 = st2.islower()
print(st2)

# ------------------------------------------------------------------------------
# startswith() and endswith() Methods
# • What is it for: Testing prefix and suffix matches in strings.
# • What it does:
#   - st3.startswith("sanG"): Checks if string starts with "sanG" (returns False because st3 has leading spaces!).
#   - st3.endswith("@123"): Checks if string ends with "@123" (returns False because st3 has trailing spaces!).
# • Where it is used: Validating URL protocols ("https://") and file extensions (".pdf", ".py").
# ------------------------------------------------------------------------------
    #startswith("") it checks is the string starting with this or not
st = st3.startswith("sanG")
print(st)
print(st3)

  #endswith("") it checks is the string endinging with this or not
st = st3.endswith("@123")
print(st)
print(st3)

# ------------------------------------------------------------------------------
# replace(old, new) Method
# • What is it for: Replacing substrings within a string.
# • What it does: Replaces all occurrences of "a" with "e".
# • Where it is used: Sanitizing strings, replacing hyphens with underscores in slugs.
# ------------------------------------------------------------------------------
    #replace("","") it replace the given string with the exixting string 
st = st3.replace("a", "e")
print(st)

# ------------------------------------------------------------------------------
# swapcase() Method
# • What is it for: Toggling casing of all letters.
# • What it does: Converts uppercase to lowercase and vice versa.
# • Where it is used: Text manipulation and stylization tools.
# ------------------------------------------------------------------------------
    #swapcase() it converts the upper case to lower to upper
st = st3.swapcase()
print(st)

# ------------------------------------------------------------------------------
# isalpha(), isdigit(), and isalnum() Validation Methods
# • What is it for: Character type validation.
# • What it does:
#   - isalpha(): Returns True only if string contains pure alphabetic letters (no numbers, spaces, or symbols).
#   - isdigit(): Returns True only if string contains pure digits.
#   - isalnum(): Returns True if string contains only alphanumeric characters (letters and digits, no spaces/symbols).
# • Where it is used: Form field validation (names, phone numbers, alphanumeric IDs).
# ------------------------------------------------------------------------------
    #isalpha it checks only is there only alphabets in the string
st = st3.isalpha()
print(st)

    #isdigit it checks only is there only alphabets in the string
st = st3.isdigit()
print(st)

    #isalnum it checks only is there only alphabets in the string
st = st3.isalnum()
print(st)

# ------------------------------------------------------------------------------
# count() and index() Methods
# • What is it for: Substring frequency counting and positional location.
# • What it does:
#   - count('a'): Counts occurrences of 'a' in st3.
#   - index('l'): Returns first index location of 'l' in st3.
# • Where it is used: Word frequency analysis, locating delimiters before slicing.
# ------------------------------------------------------------------------------
    #count("") it tell how many times the string is present
st = st3.count('a')
print(st)

    #index("") first occuring position of th string
st = st3.index('l')
print(st)

# ------------------------------------------------------------------------------
# lstrip(), rstrip(), and strip() Whitespace Trimming
# • What is it for: Trimming extraneous leading and trailing whitespace characters.
# • What it does:
#   - lstrip(): Strips spaces from the left side only.
#   - rstrip(): Strips spaces from the right side only.
#   - strip(): Strips spaces from both left and right sides.
# • Where it is used: Sanitizing user inputs from text fields and cleaning scraped web data.
# ------------------------------------------------------------------------------
    #lstrip() it removes the left side space only
st = st3.lstrip()
print(st)

    #rstrip() it removes the right side space only
st = st3.rstrip()
print(st)

    #strip() removes the space in from right and left
st = st3.strip()
print(st)

# ------------------------------------------------------------------------------
# String Slicing [start:stop:step]
# • What is it for: Extracting specific portions or patterns of characters from a string.
# • What it does:
#   - st4[:8]: Extracts indices 0 through 7 (first 8 characters).
#   - st4[5:]: Extracts from index 5 through the end.
#   - st4[6:25]: Extracts from index 6 through 24 (25 is exclusive).
#   - st4[::2]: Steps through the string with stride 2, extracting every second character.
# • Where it is used: Extracting date components, parsing fixed-width data files, masking card numbers.
# ------------------------------------------------------------------------------
st4 = "0123456789012345678901234567890"
    #sclice means [start:end]Start = start,ends =end+1
print(st4[:8]) #from the postion 8 onword it wont print any thing
print(st4[5:]) # it leaves first 4 numbers ,5 and after that it will print
print(st4[6:25]) #it print position number 6 to 24 , 25  will not print i told first end =end+1
print(st4[::2]) #it prints only 0 2 4 because it skips one place
