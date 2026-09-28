# ==============================================================================
# Module: typecasting3.py
# Topic: Inter-Collection Typecasting (list, tuple, set, dict, and str conversions)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Converting a List to other Data Structures
# • What is it for: Changing mutable list collections into immutable or unique structures.
# • What it does:
#   - tuple(l): Converts [10, 20, 30] to immutable (10, 20, 30).
#   - set(l): Converts to {10, 20, 30}, stripping any duplicate values.
#   - str(l): Converts list into a literal string representation "[10, 20, 30]".
#   - dict(l) fails because each element must be a (key, value) pair.
# • Where it is used: Freezing a list into a tuple for hashable dictionary keys, deduplicating with set().
# ------------------------------------------------------------------------------
l = [10, 20, 30]
print(tuple(l))
print(set(l))
print(str(l))
#print(dict(l))

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 2. Converting a Tuple to other Data Structures
# • What is it for: Unfreezing an immutable tuple so its items can be altered, or deduplicating it.
# • What it does:
#   - set(t): Converts (10, 20, 30) into unique set {10, 20, 30}.
#   - list(t): Converts tuple into mutable list [10, 20, 30] allowing append/remove.
#   - str(t): Converts into literal string "(10, 20, 30)".
# • Where it is used: Converting read-only database query rows into editable lists for processing.
# ------------------------------------------------------------------------------
t = (10, 20, 30)
print(set(t))
print(list(t))
print(str(t))
#print(dict(t))

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 3. Converting a Set to other Data Structures
# • What is it for: Giving order or indexability to an unordered set.
# • What it does:
#   - list(s): Converts set into an indexable list [10, 20, 30] (order is arbitrary).
#   - tuple(s): Converts set into an immutable, indexable tuple (10, 20, 30).
#   - str(s): Converts set into string "{10, 20, 30}".
# • Where it is used: Accessing set items by index (s[0] is illegal, but list(s)[0] works!).
# ------------------------------------------------------------------------------
s = {10, 20, 30}
print(list(s))
print(tuple(s))
print(str(s))
#print(dict(s))

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 4. Converting a String into Collections
# • What is it for: Breaking down a string into individual character tokens.
# • What it does:
#   - list('python'): Returns individual characters ['p', 'y', 't', 'h', 'o', 'n'].
#   - tuple('python'): Returns immutable characters ('p', 'y', 't', 'h', 'o', 'n').
#   - set('python'): Returns set of unique characters (removes any repeat letters).
# • Where it is used: Anagram checking, counting unique letters, letter-frequency analysis.
# ------------------------------------------------------------------------------
#s1 = '10','20','30'
s1 = 'python'
print(list(s1))
print(tuple(s1))
print(set(s1))
#print(dict(s1))

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 5. Converting a Dictionary into Collections
# • What is it for: Extracting dictionary components (keys, values) into standard sequences.
# • What it does:
#   - list(d.values()): Extracts just the values [2, 4, 6] as a list.
#   - tuple(d): By default iterates over dictionary KEYS -> (1, 3, 5).
#   - set(d): Returns unique dictionary KEYS -> {1, 3, 5}.
#   - str(d): Serializes the entire dictionary into a string "{1: 2, 3: 4, 5: 6}".
# • Where it is used: Exporting table headers from dictionary keys, generating value charts from values.
# ------------------------------------------------------------------------------
d = {
    1: 2,
    3: 4,
    5: 6
}

print(list(d.values()))
print(tuple(d))
print(set(d))
print(str(d))

print("----------------------------------------")
