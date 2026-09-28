# ==============================================================================
# Module: tuple_datatype.py
# Topic: Python Tuples: Creation, Length, Single-Element Syntax, and Immutability
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Empty Tuple Creation and type() Inspection
# • What is it for:
#   Creating an immutable (read-only) ordered sequence of elements using parentheses ().
# • What it does:
#   - tup = () initializes an empty tuple.
#   - type(tup) returns <class 'tuple'>.
# • Where it is used:
#   Returning multiple values from functions, fixed database lookup tables, dictionary keys.
# ------------------------------------------------------------------------------
tup = () # create the tuple using the ()
print(tup)
dt = type(tup) #find the data type of the variable type()
print(dt)

print("-----------------------------------")

# ------------------------------------------------------------------------------
# 2. Measuring Tuple Size with len()
# • What is it for: Determining the total number of elements contained in the tuple.
# • What it does: len(tup) calculates item count (0 for empty tuple).
# • Where it is used: Boundary checks, validating coordinate pair dimensions (e.g., verifying len == 2 for x, y).
# ------------------------------------------------------------------------------
# used to show the how many elements are present in the tuple using len()
print(len(tup))
#or
a = len(tup)
print(a)
print("-----------------------------------")

# ------------------------------------------------------------------------------
# 3. Multi-Element Homogeneous Tuple
# • What is it for: Storing multiple ordered elements.
# • What it does: Holds 4 integers (11, 22, 33, 54), type is tuple, size is 4.
# • Where it is used: Storing RGB color codes (255, 128, 0), fixed dimension sizes (1920, 1080).
# ------------------------------------------------------------------------------
t3 = (11, 22, 33, 54)
dt1 = type(t3)
size = len(t3)
print(dt1)
print(size)
print("-----------------------------------")

# ------------------------------------------------------------------------------
# 4. Single-Element Tuple Syntax (Trailing Comma Requirement)
# • What is it for: Correctly creating a tuple with only one element.
# • What it does:
#   In Python, parentheses are also used for mathematical grouping. Therefore:
#     (50)   -> evaluated as integer int 50
#     (50,)  -> recognized as a single-element tuple!
# • Where it is used: Passing single parameters to SQL query parameters (cursor.execute("SELECT * WHERE id=?", (user_id,))),
#   single-argument thread target functions.
# ------------------------------------------------------------------------------
#t4=(50) if you check the data type of this it gives as int data type but you need it in the tuple so you have to add , comma
#if you want it as the tuple in python 
#we need to place a comma at the end ,when we have the single element
#inside the tuple
t4 = (50,)
dt2 = type(t4)
print(dt2)
print("-----------------------------------")

# ------------------------------------------------------------------------------
# 5. Heterogeneous Data, Negative Indexing, and Immutability
# • What is it for: Storing mixed data types securely without risk of accidental mutation.
# • What it does:
#   - Contains int, complex (63j), bool (True), and float (45.5).
#   - Negative index t5[-2] accesses the second element from the end (True).
#   - Tuples are IMMUTABLE: Attempting t5[6] = 100 raises TypeError: 'tuple' object does not support item assignment.
# • Where it is used:
#   Database record rows (e.g. (user_id, name, is_active, balance)) where fields should not be altered accidentally.
# ------------------------------------------------------------------------------
t5 = (23, 33, 4, 3, 53, 63j, True, 45.5)
ind = t5[-2]
print(ind)
print(t5)
# t5[6]=100 TypeError: 'tuple' object does not support item assignment because IMMUTABLE
print("-----------------------------------")
