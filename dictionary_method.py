# ==============================================================================
# Module: dictionary_method.py
# Topic: Built-in Dictionary Methods (setdefault, update, get, pop, popitem, keys, values, items)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. setdefault(key, default=None) Method
# • What is it for: Safely inserting a key with a default value only if the key is not already present.
# • What it does:
#   - d.setdefault(11, 200): Key 11 is absent, so adds 11: 200.
#   - d.setdefault(22): Key 22 is absent, so adds 22: None.
#   - d.setdefault(22, 400): Key 22 already exists, so it leaves 22: None unchanged (does not overwrite!).
# • Where it is used: Initializing grouping dictionaries (e.g. word counts, lists of users per department).
# ------------------------------------------------------------------------------
# setdefault
d = {}
d.setdefault(11, 200)
d.setdefault(22)
d.setdefault(22, 400)
print(d)

print("--------------------------------------")

# ------------------------------------------------------------------------------
# 2. update() Method
# • What is it for: Merging key-value pairs from another dictionary into the existing dictionary.
# • What it does: Takes all pairs from d2 ({22:33, 44:55, 66:77}) and inserts/updates them into d1.
# • Where it is used: Merging default settings with user-customized preferences.
# ------------------------------------------------------------------------------
#update it combines the bothe dictionary
d1 = {11: 12, 13: 14, 15: 16}
d2 = {22: 33, 44: 55, 66: 77}
d1.update(d2)
print(d1)

print("--------------------------------------")

# ------------------------------------------------------------------------------
# 3. get(key, default=None) Method
# • What is it for: Safely accessing the value of a key without risking a program crash.
# • What it does:
#   - d2.get(44): Key 44 exists -> returns 55.
#   - d2.get(88): Key 88 does not exist -> returns None (instead of crashing with KeyError!).
# • Where it is used: Reading optional API response parameters or optional configuration settings.
# ------------------------------------------------------------------------------
#get method it access the particular key of the value
d2 = {22: 33, 44: 55, 66: 77}
val1 = d2.get(44)
val2 = d2.get(88)
print(val1)
print(val2)

print("--------------------------------------")

# ------------------------------------------------------------------------------
# 4. pop(key) Method
# • What is it for: Removing a specific key and retrieving its value simultaneously.
# • What it does: Removes key 13.5 from d5, returns its value 135, and mutates d5 in-place.
# • Where it is used: Processing and removing a token, consuming an authorization code.
# ------------------------------------------------------------------------------
#pop it will delete the particular key and value
d5 = {12.4: 124, 13.5: 135}
pv = d5.pop(13.5)
print(pv)
print(d5)

print("--------------------------------------")

# ------------------------------------------------------------------------------
# 5. popitem() Method
# • What is it for: Removing and returning the last inserted key-value pair as a tuple (key, value).
# • What it does: In Python 3.7+, dictionaries are insertion-ordered.
#   popitem() pops the most recently inserted pair (2, 3) from d6.
# • Where it is used: Cache eviction policies (like LRU caches), processing tasks in LIFO order.
# ------------------------------------------------------------------------------
d6 = {1: 4, 5: 7, 6: 8, 2: 3}
val3 = d6.popitem()
print(val3)
print(d6)

print("--------------------------------------")

# ------------------------------------------------------------------------------
# 6. keys() View Method
# • What is it for: Providing a dynamic view of all keys present in the dictionary.
# • What it does: Returns dict_keys([1, 5, 6]). Reflects any future updates to d6 immediately.
# • Where it is used: Iterating over all available field names, checking valid column headers.
# ------------------------------------------------------------------------------
ks = d6.keys()
print(ks)

print("--------------------------------------")

# ------------------------------------------------------------------------------
# 7. values() View Method
# • What is it for: Providing a dynamic view of all values stored in the dictionary.
# • What it does: Returns dict_values([4, 7, 8]).
# • Where it is used: Computing summary statistics (sum, average) over numerical values in a record.
# ------------------------------------------------------------------------------
vs = d6.values()
print(vs)

print("--------------------------------------")

# ------------------------------------------------------------------------------
# 8. items() View Method
# • What is it for: Providing a dynamic view of all (key, value) pairs as tuples.
# • What it does: Returns dict_items([(1, 4), (5, 7), (6, 8)]).
# • Where it is used: Looping over both keys and values simultaneously (e.g., for key, value in d.items(): ...).
# ------------------------------------------------------------------------------
it = d6.items()
print(it)

print("--------------------------------------")
