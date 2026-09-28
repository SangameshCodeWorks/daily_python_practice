# ==============================================================================
# Module: string_datatype.py
# Topic: String Creation and Positive Indexing
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. String Creation with Mixed Characters
# • What is it for:
#   Storing alphanumeric text, symbols, and special characters in an immutable sequence.
# • What it does:
#   Creates string variable 's1' containing letters, digits, and special characters ('@', '$', '%'),
#   and outputs it to the console.
# • Where it is used:
#   Storing passwords, email hashes, product serial keys, usernames, and raw text data.
# ------------------------------------------------------------------------------
s1 = 'sanga@34$%gmASD'
print(s1)

print("--------------------------------------------")

# ------------------------------------------------------------------------------
# 2. String Indexing (Zero-Based Positive Index)
# • What is it for:
#   Accessing an individual character within a string by its positional offset.
# • What it does:
#   In 'Python':
#     Index 0 -> 'P'
#     Index 1 -> 'y'
#     Index 2 -> 't'
#     Index 3 -> 'h'
#     Index 4 -> 'o'
#     Index 5 -> 'n'
#   s2[2] retrieves and prints the character at index 2, which is 't'.
# • Where it is used:
#   Extracting initials from a name (e.g. name[0]), parsing fixed-width text files,
#   inspecting specific characters like prefixes or file extension codes.
# ------------------------------------------------------------------------------
s2 = 'Python'
print(s2[2])
