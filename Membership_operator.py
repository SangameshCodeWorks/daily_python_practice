# ==============================================================================
# Module: Membership_operator.py
# Topic: Membership Operators ('in' and 'not in') Across Python Collections
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Membership in Lists
# • What is it for:
#   Checking whether an element exists inside an ordered sequence (List).
# • What it does:
#   Linearly scans the list to match the target element:
#   - 4 in [1, 3, 5, 6] -> False (4 is absent)
#   - 5 in [1, 3, 5, 6] -> True  (5 is present)
# • Where it is used:
#   Verifying user roles in an allowed roles list, search filters, form validation.
# ------------------------------------------------------------------------------
# Membership operator with List
print(4 in [1, 3, 5, 6])        # Result: False
print(5 in [1, 3, 5, 6])        # Result: True

print("---------------------------------------")

# ------------------------------------------------------------------------------
# 2. Membership in Tuples
# • What is it for:
#   Verifying existence of an item inside an immutable sequence (Tuple).
# • What it does:
#   Evaluates whether 11 is contained within (10, 11, 12, 13) -> True.
# • Where it is used:
#   Checking valid HTTP status codes (status in (200, 201, 204)), allowed file extensions.
# ------------------------------------------------------------------------------
# Membership operator with Tuple
print(11 in (10, 11, 12, 13))   # Result: True


# ------------------------------------------------------------------------------
# 3. Membership in Sets
# • What is it for:
#   Ultra-fast O(1) average time hash lookup to test if an element is in a Set.
# • What it does:
#   Hashes the float 11.1 and checks against {11, 0.1, 11.4} -> False (not in set).
# • Where it is used:
#   High-performance deduplication checks, blacklist/whitelist lookup tables.
# ------------------------------------------------------------------------------
# Membership operator with Set
print(11.1 in {11, 0.1, 11.4})  # Result: False


# ------------------------------------------------------------------------------
# 4. Membership in Strings (Substring Search)
# • What is it for:
#   Checking whether a character or contiguous substring exists within a string.
# • What it does:
#   Checks if "ja" is a substring of "java" -> True.
# • Where it is used:
#   Searching for keywords, profanity/spam filtering, URL parameter validation.
# ------------------------------------------------------------------------------
# Membership operator with String
print("ja" in "java")           # Result: True

print("---------------------------------------")

# ------------------------------------------------------------------------------
# 5. Crucial Gotcha: Membership in Dictionaries (Keys vs Values vs Items)
# • What is it for:
#   Understanding how the 'in' operator behaves when applied to dictionaries.
# • What it does:
#   - 'key in dict': By default, 'in' checks DICTIONARY KEYS only!
#     20 in {2: 20, 3: 30, 4: 40} -> False, because 20 is a VALUE, not a KEY (keys are 2, 3, 4).
#   - 'val in dict.items()': Checks if target matches full (key, value) pairs.
#     20 in d.items() -> False, because items contains tuples like (2, 20), not scalar 20.
#     (To check values, use '20 in d.values()' -> True).
# • Where it is used:
#   Checking if a config key or header exists in payload dictionaries before accessing it.
# ------------------------------------------------------------------------------
# Dict membership default: checks keys, not values!
print(20 in {2: 20, 3: 30, 4: 40})  # Result: False (20 is a value; keys are 2, 3, 4)

d = {2: 20, 3: 30, 4: 40}
print(20 in d.items())              # Result: False (items are (key, val) tuples: (2, 20), (3, 30), (4, 40))
