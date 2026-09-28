# ==============================================================================
# Module: sample1.py
# Topic: Variables, Reassignment, and Memory Management with id()
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Single-Line Comments and Variable Initialization
# • What is it for:
#   Comments (#) are used for documentation and notes that the Python interpreter ignores.
#   Variable assignment binds a name (identifier) to a value stored in memory.
# • What it does:
#   Creates variable 'a' in memory, stores integer 10, and prints its value to console.
# • Where it is used:
#   Everywhere in code to store temporary or persistent values like counts, configurations,
#   user details, and mathematical constants.
# ------------------------------------------------------------------------------
#single line comment
a = 10
print(a)

# ------------------------------------------------------------------------------
# 2. Variable Reassignment / Updating Values
# • What is it for:
#   To update the state or value referenced by a variable over time.
# • What it does:
#   First assigns 20 to 'b'. Then reassigns 30 to 'b', so the reference changes to 30.
#   Printing 'b' displays the updated value 30.
# • Where it is used:
#   Counters in loops, game scores, accumulator totals, tracking changed user inputs,
#   and updating object states.
# ------------------------------------------------------------------------------
b = 20
b = 30
print(b)

# ------------------------------------------------------------------------------
# 3. Object Referencing and Integer Caching (Interning)
# • What is it for:
#   Understanding how Python manages memory for identical immutable literals.
# • What it does:
#   Assigns 50 to both 'c' and 'd'. In CPython, small integers (-5 to 256) are interned
#   (cached), meaning both variables point to the exact same memory address.
# • Where it is used:
#   Python internal memory optimization to save RAM when frequently used numbers or
#   strings appear across applications.
# ------------------------------------------------------------------------------
c = 50
d = 50
print("C:", c)
print("D:", d)

# ------------------------------------------------------------------------------
# 4. id() Function and Memory Addresses
# • What is it for:
#   To retrieve the unique memory address (identity) of an object in RAM.
# • What it does:
#   id(d) and id(c) return the memory addresses of variables 'd' and 'c'.
#   Since both hold integer 50, both IDs will be identical.
# • Where it is used:
#   Debugging memory leaks, verifying shallow vs deep copies, understanding object
#   mutability vs immutability, and checking if two references point to the same object.
# ------------------------------------------------------------------------------
address = id(d)
address1 = id(c)
print("D", address)
print("C", address1)
