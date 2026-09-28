# ==============================================================================
# Module: set_datatype.py
# Topic: Python Sets: Creation, Unordered Nature, and Unique Element Constraints
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Empty Set Creation using set()
# • What is it for:
#   Creating a collection of unique, unordered elements.
# • What it does:
#   - Note: {} creates an empty dictionary, so you MUST use set() to create an empty set.
#   - type(s) confirms <class 'set'>.
# • Where it is used:
#   Accumulating unique items dynamically (e.g., unique visitor IP addresses, active tags).
# ------------------------------------------------------------------------------
s = set()
print(s)
print(type(s))
print("---------------------------------------")

# ------------------------------------------------------------------------------
# 2. Set Literal and Size with len()
# • What is it for: Initializing a set with values and inspecting its length.
# • What it does: Creates set s1 containing 5 numbers. len(s1) returns 5.
# • Where it is used: Fast membership testing (checking if an ID exists in O(1) time).
# ------------------------------------------------------------------------------
s1 = {10, 20, 30, 40, 50}
print(len(s1))
print(s1)

print("---------------------------------------")

# ------------------------------------------------------------------------------
# 3. Unordered Nature and Automatic Deduplication
# • What is it for: Removing duplicates automatically and handling mixed hashable data types.
# • What it does:
#   - Contains duplicate 20 (entered twice); Python automatically keeps only one 20.
#   - Does not maintain insertion order; items are arranged based on internal hash values.
#   - Supports heterogeneous hashable types: int, str, float, bool, None, complex.
# • Where it is used:
#   Deduplicating lists of IDs or emails, filtering out repeat user votes, tag clouds.
# ------------------------------------------------------------------------------
s2 = {20, "Raj", 20.2, True, None, 30j, 20}
print(s2)
#unorder and duplicates are not allowed
print("---------------------------------------")
