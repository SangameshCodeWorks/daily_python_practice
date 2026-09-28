# ==============================================================================
# Module: typecasting4.py
# Topic: Collection Truthiness (bool) and String-to-Numeric Parsing
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Truthiness of Non-Empty Collections
# • What is it for: Checking whether a collection contains elements or is empty.
# • What it does:
#   In Python, any non-empty container (list, tuple, string, set, dict) evaluates to True.
#   Empty containers ([], (), "", set(), {}) evaluate to False.
#   - bool([10, 20]) -> True (non-empty list)
#   - bool((11, 33)) -> True (non-empty tuple)
#   - bool("try")    -> True (non-empty string)
#   - bool({12, 15}) -> True (non-empty set)
#   - bool({1:2, 1:3}) -> True (contains {1: 3}, key 1 overwritten by 3)
# • Where it is used:
#   Simplifying conditionals: if users_list: process_users() instead of if len(users_list) > 0.
# ------------------------------------------------------------------------------
l1 = [10, 20]
print(bool(l1))

t1 = (11, 33)
print(bool(t1))

s1 = "try"
print(bool(s1))

ss1 = {12, 15}
print(bool(ss1))

d1 = {1: 2, 1: 3}
print(bool(d1))

print("-----------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Parsing Numeric Strings into Scalar Data Types
# • What is it for: Converting user text input or file data into numeric values for computation.
# • What it does:
#   - int('10'): Parses integer string into int 10.
#   - float('1.0'): Parses floating-point string into float 1.0.
#   - complex('1j'): Parses complex notation string into complex 1j (0+1j).
# • Where it is used:
#   Parsing values from CSV files, JSON payloads, HTTP query parameters, or terminal input.
# ------------------------------------------------------------------------------
s1 = '10'
i = int(s1)
print(i)

f1 = '1.0'
f = float(f1)
print(f)
print(type(f))

c1 = '1j'
c = complex(c1)
print(c)
print(type(c))
