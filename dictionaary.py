# ==============================================================================
# Module: dictionaary.py
# Topic: Python Dictionaries: Key-Value Mapping, Accessing, Updating, and Insertion
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Empty Dictionary Creation and type() Inspection
# • What is it for: Initializing an empty hash map (key-value store).
# • What it does:
#   - {} creates an empty dictionary.
#   - type(d1) returns <class 'dict'>.
# • Where it is used: Building configurations, JSON objects, response payload containers.
# ------------------------------------------------------------------------------
d1 = {}
print(d1)
print(type(d1))
print("-------------------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Dictionary Size with len()
# • What is it for: Measuring the number of key-value pairs present.
# • What it does: len(d1) counts pairs (0 for an empty dictionary).
# • Where it is used: Verifying non-empty payloads, checking if cache contains entries.
# ------------------------------------------------------------------------------
d2 = {}
print(len(d1))

print("-------------------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Initializing Key-Value Pairs
# • What is it for: Mapping unique keys to their associated values.
# • What it does: Maps numbers (12, 13, 14, 15) to their squares (144, 169, 196, 225).
# • Where it is used: Fast O(1) lookups by ID, product price tables, phonebooks.
# ------------------------------------------------------------------------------
d3 = {
    12: 144,
    13: 169,
    14: 196,
    15: 225
}
print(d3)

print("-------------------------------------------------------------")

# ------------------------------------------------------------------------------
# 4. Accessing Value by Key (Bracket Notation)
# • What is it for: Retrieving the value associated with a specific key.
# • What it does: Looks up key 14 in 'd3' and returns 196. Note: Raises KeyError if key does not exist.
# • Where it is used: Fetching user details by ID, getting product price by SKU code.
# ------------------------------------------------------------------------------
s1 = d3[14]
print(s1)

# ------------------------------------------------------------------------------
# 5. Modifying Existing Key's Value
# • What is it for: Updating the value linked to an existing key.
# • What it does: Overwrites the value of key 15 from 225 to 200.
# • Where it is used: Updating account balances, changing user settings, modifying order status.
# ------------------------------------------------------------------------------
d3[15] = 200
print(d3)

# ------------------------------------------------------------------------------
# 6. Adding a New Key-Value Pair
# • What is it for: Dynamically inserting a new key and value into the dictionary.
# • What it does: Since key 16 doesn't exist in 'd3', Python adds key 16 with value 1000.
# • Where it is used: Caching new query results, adding new fields to an active user session.
# ------------------------------------------------------------------------------
d3[16] = 1000
print(d3)
