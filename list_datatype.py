# ==============================================================================
# Module: list_datatype.py
# Topic: Python List Data Structure, Negative Indexing, and Mutability
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. List Creation (Literal vs Constructor)
# • What is it for:
#   Storing an ordered, mutable (changeable) collection of items.
# • What it does:
#   - nums = [10, 20, 30, 40, 50, 60]: Initializes list with numbers.
#   - nums1 = []: Creates empty list using literal syntax.
#   - nums2 = list(): Creates empty list using the built-in constructor.
# • Where it is used:
#   Collecting dynamic data (shopping carts, user feeds, search results, queues).
# ------------------------------------------------------------------------------
nums = [10, 20, 30, 40, 50, 60]
nums1 = []
nums2 = list()

# ------------------------------------------------------------------------------
# 2. type() Inspection and Printing
# • What is it for: Verifying the data type and viewing list contents.
# • What it does: type(nums) returns <class 'list'> confirming it is a Python list object.
# • Where it is used: Runtime debugging, asserting valid parameter types in functions.
# ------------------------------------------------------------------------------
var = type(nums)
print(var)
print(nums2)
print(nums1)
print(nums)

# ------------------------------------------------------------------------------
# 3. Negative Indexing
# • What is it for: Accessing elements from the end of a list without knowing its exact length.
# • What it does:
#   In nums [10, 20, 30, 40, 50, 60]:
#     -1 is 60 (last)
#     -2 is 50 (second from end)
#     -3 is 40 (third from end)
#     -4 is 30 (fourth from end)
#   nums[-4] prints 30; nums[-2] prints 50.
# • Where it is used:
#   Getting the most recent transaction, reading the latest added user, trailing elements.
# ------------------------------------------------------------------------------
print(nums[-4])
print(nums[-2])

# ------------------------------------------------------------------------------
# 4. Mutability (In-Place Item Assignment)
# • What is it for: Modifying existing elements within the list directly in memory.
# • What it does: Replaces the element at index -4 (previously 30) with 80 -> [10, 20, 80, 40, 50, 60].
# • Where it is used: Updating user records, modifying scores in a game, editing spreadsheet cells.
# ------------------------------------------------------------------------------
nums[-4] = 80
print(nums)
