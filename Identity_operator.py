# ==============================================================================
# Module: Identity_operator.py
# Topic: Identity Operators (is, is not) and Identity vs Equality (is vs ==)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Identity Operator: 'is' (Same Memory Reference)
# • What is it for:
#   Checks whether two variables refer to the EXACT SAME object in memory (id(a) == id(b)).
# • What it does:
#   When 'b = a' is executed, 'b' is assigned the memory reference of 'a'.
#   Therefore, 'a is b' returns True because both variables point to the same memory address.
# • Where it is used:
#   Checking singletons like 'x is None', verifying object aliasing, caching checks.
# ------------------------------------------------------------------------------
# Identity operator: same object reference
a = 4
b = a
print(a is b)       # Result: True (both reference the same integer object in memory)

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Identity Operator: 'is' with Distinct Objects
# • What is it for:
#   Determining if two variables refer to separate, distinct objects in memory.
# • What it does:
#   'c' holds 10 and 'd' holds 11. They are distinct objects with different memory IDs.
#   Therefore, 'c is d' evaluates to False.
# • Where it is used:
#   Verifying distinct entity instances, ensuring separate memory allocations.
# ------------------------------------------------------------------------------
c = 10
d = 11
print(c is d)       # Result: False (different memory locations)

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Negated Identity Operator: 'is not'
# • What is it for:
#   Checks whether two variables do NOT refer to the same object in memory.
# • What it does:
#   Since 'a' and 'b' reference the exact same object, 'a is not b' returns False.
# • Where it is used:
#   Validating that an optional argument or return value is not None (if val is not None).
# ------------------------------------------------------------------------------
print(a is not b)   # Result: False (because a and b ARE the same object)

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 4. Crucial Concept: Identity ('is') vs Equality ('==') with Mutable Collections
# • What is it for:
#   Differentiating between object identity (memory address) and value equivalence (contents).
# • What it does:
#   - 'l1' and 'l2' are independently created list objects with identical contents [10, 20, 30].
#   - 'l1 is l2' -> False: Python creates two distinct list objects at different memory addresses.
#   - 'l1 == l2' -> True: The '==' operator compares their values/elements, which are identical.
# • Where it is used:
#   Crucial in preventing unintended side-effects when mutating shared references vs copied lists,
#   and writing correct unit test assertions.
# ------------------------------------------------------------------------------
l1 = [10, 20, 30]
l2 = [10, 20, 30]

print(l1 is l2)     # Result: False (different memory locations: id(l1) != id(l2))
print(l1 == l2)     # Result: True (contents/values are identical)

print("------------------------------------------------")
