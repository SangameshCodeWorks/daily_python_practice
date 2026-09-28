# ==============================================================================
# Module: String_methods.py
# Topic: Built-in Python String Methods (Case, Validation, Search, Split & Join)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. capitalize() Method
# • What is it for: Capitalizing only the very first character of the string.
# • What it does: Converts the first letter to uppercase and all remaining letters to lowercase -> "Krishan".
# • Where it is used: Formatting names, sentences, or user-submitted text for uniform presentation.
# ------------------------------------------------------------------------------
s1 = "krishan"
print(s1.capitalize())
print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. title() Method
# • What is it for: Converting string to title case (capitalizing first letter of each word).
# • What it does: Capitalizes every word following a space or punctuation -> "Tomarrow Is Saturday".
# • Where it is used: Formatting book titles, article headings, person names, address lines.
# ------------------------------------------------------------------------------
s2 = "tomarrow is saturday"
print(s2.title())

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. upper() and isupper() Methods
# • What is it for: Converting to uppercase and testing uppercase status.
# • What it does:
#   - upper(): Returns a copy of "benedict" with all letters in uppercase -> "BENEDICT".
#   - isupper(): Returns True if all alphabetic characters are uppercase; False otherwise -> False on original s3.
# • Where it is used: Case-insensitive comparisons (e.g. state codes "CA", SQL keywords, promo codes).
# ------------------------------------------------------------------------------
s3 = "benedict"
print(s3.upper())
print(s3.isupper())

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 4. lower() Method
# • What is it for: Converting all uppercase characters to lowercase.
# • What it does: Converts "TOMARROW IS GANESHA FESTIVAL" -> "tomarrow is ganesha festival".
# • Where it is used: Normalizing email addresses, usernames, and search keywords for database queries.
# ------------------------------------------------------------------------------
s4 = "TOMARROW IS GANESHA FESTIVAL"
print(s4.lower())

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 5. islower() Method
# • What is it for: Checking whether all alphabetic characters in the string are lowercase.
# • What it does: Returns True if there are lowercase letters and no uppercase letters -> True for s2.
# • Where it is used: Password policy checks (ensuring mix of cases), input validation.
# ------------------------------------------------------------------------------
print(s2.islower())
print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 6. startswith() Method
# • What is it for: Verifying if a string starts with a specified prefix substring.
# • What it does: Evaluates whether "Hello Get Lost" begins with "H" -> True.
# • Where it is used: Checking URL protocols ("https://"), file name prefixes, international phone country codes.
# ------------------------------------------------------------------------------
s5 = "Hello Get Lost"
print(s5.startswith("H"))

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 7. replace(old, new) Method
# • What is it for: Replacing all occurrences of a specified substring with a new substring.
# • What it does: Scans 'hahaha' and replaces every 'a' with 'e' -> 'hehehe'.
# • Where it is used: Cleaning messy text data, censoring profanity, replacing dashes with slashes in dates.
# ------------------------------------------------------------------------------
print("------------------------------------------------")
s6 = ('hahaha')
print(s6.replace('a', 'e'))

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 8. swapcase() Method
# • What is it for: Inverting the letter casing of all alphabetic characters.
# • What it does: Converts uppercase to lowercase and lowercase to uppercase ("Good Morning" -> "gOOD mORNING").
# • Where it is used: Handling accidental Caps Lock toggling, specialized text effects, cryptographic obfuscation.
# ------------------------------------------------------------------------------
s7 = "Good Morning"
print(s7.swapcase())

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 9. isalpha() Method
# • What is it for: Checking if the string contains ONLY alphabetic letters (A-Z, a-z).
# • What it does: Checks "mahesh04@gmail.com". Because it contains digits ('04') and symbols ('@', '.'), returns False.
# • Where it is used: Validating person first/last names (ensuring no numbers or symbols were entered).
# ------------------------------------------------------------------------------
s8 = "mahesh04@gmail.com"
print(s8.isalpha())

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 10. isdigit() Method
# • What is it for: Checking if the string contains ONLY numeric digits (0-9).
# • What it does: Checks "995864733"; since every character is a digit, returns True.
# • Where it is used: Validating phone numbers, PIN codes, OTP inputs, credit card numbers before parsing.
# ------------------------------------------------------------------------------
s9 = "995864733"
print(s9.isdigit())

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 11. isalnum() Method
# • What is it for: Checking if the string contains only alphanumeric characters (letters and numbers).
# • What it does: Checks "cdds56re122"; contains only letters and digits without symbols/spaces -> True.
# • Where it is used: Validating alphanumeric usernames, passwords requiring alphanumeric characters, vehicle license plates.
# ------------------------------------------------------------------------------
s10 = "cdds56re122"
print(s10.isalnum())

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 12. count() Method
# • What is it for: Counting the number of non-overlapping occurrences of a substring.
# • What it does:
#   - count('A'): Counts single 'A' occurrences in "FAAANTAA" -> 5.
#   - count("AA"): Counts pairs of "AA" without overlapping -> 2 ("AA" from index 1-2, and index 6-7).
# • Where it is used: Keyword density analysis in SEO, counting DNA codons, frequency analysis in security logs.
# ------------------------------------------------------------------------------
s11 = "FAAANTAA"
print(s11.count('A'))
print(s11.count("AA"))

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 13. index() Method
# • What is it for: Finding the zero-based index of the first occurrence of a substring.
# • What it does: Finds the first index where "AA" starts in "FAAANTAA" -> returns 1.
# • Where it is used: Locating delimiters, extracting tokens after a known keyword or tag.
# ------------------------------------------------------------------------------
print(s11.index('AA'))

# ------------------------------------------------------------------------------
# 14. split() Method (Default Whitespace)
# • What is it for: Splitting a string into a list of words using whitespace (spaces, tabs, newlines).
# • What it does: Splits "Good day everyone how are you" into ['Good', 'day', 'everyone', 'how', 'are', 'you'].
# • Where it is used: Natural language processing (tokenizing sentences into words), parsing command arguments.
# ------------------------------------------------------------------------------
#split()method
s12 = "Good day everyone how are you"
word = s12.split()
print(word)

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 15. split() with Custom Delimiter (Comma)
# • What is it for: Splitting text separated by a specific character (like a comma).
# • What it does: Breaks "karthik,durga,shravani" by comma into ['karthik', 'durga', 'shravani'].
# • Where it is used: Parsing CSV (comma-separated values) data rows, tagging systems, user list imports.
# ------------------------------------------------------------------------------
s13 = "karthik,durga,shravani"
word2 = s13.split(",")
print(word2)

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 16. split() with Slash Delimiter
# • What is it for: Splitting date or path strings separated by forward slashes.
# • What it does: Breaks "21/09/2026" by "/" into ['21', '09', '2026'].
# • Where it is used: Extracting day, month, and year components from date strings, parsing URL paths.
# ------------------------------------------------------------------------------
s14 = "21/09/2026"
word4 = s14.split("/")
print(word4)

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 17. join() Method with Space Delimiter
# • What is it for: Joining an iterable (like a list) of strings into a single string.
# • What it does: Concatenates ['apple', 'mango', 'banana'] with space " " separator -> "apple mango banana".
# • Where it is used: Rebuilding sentences from word tokens, creating readable lists in user interfaces.
# ------------------------------------------------------------------------------
l1 = ['apple', 'mango', 'banana']
s15 = " ".join(l1)
print(s15)

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 18. join() Method with Custom Slash Delimiter
# • What is it for: Joining a list of date parts or path components with slashes.
# • What it does: Joins ['15', '08', '1947'] using "/" -> "15/08/1947".
# • Where it is used: Formatting dates for display or storage, creating filesystem paths, constructing URL routes.
# ------------------------------------------------------------------------------
date = ['15', '08', '1947']
st16 = "/".join(date)
print(st16)
