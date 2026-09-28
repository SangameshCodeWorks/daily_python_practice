# ==============================================================================
# Module: charactertoUnicode.py
# Topic: Character Encoding & Decoding with ord() and chr()
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. ord() Function (Character to Unicode / ASCII Code Point)
# • What is it for:
#   To convert a single string character into its corresponding integer Unicode/ASCII value.
# • What it does:
#   Looks up the character in the Unicode table and returns its numeric code:
#   - Uppercase 'A' to 'Z' map to 65 through 90
#   - Lowercase 'a' to 'z' map to 97 through 122
#   - Digits '0' to '9' map to 48 through 57
#   - Space character ' ' maps to 32
# • Where it is used:
#   Building custom ciphers (Caesar cipher / cryptography), custom sorting algorithms,
#   input sanitization, case-conversion algorithms without built-in methods.
# ------------------------------------------------------------------------------
print(ord("A"))  # Returns 65 (ASCII for uppercase 'A')
print(ord("Z"))  # Returns 90 (ASCII for uppercase 'Z')

print(ord("a"))  # Returns 97 (ASCII for lowercase 'a')
print(ord("z"))  # Returns 122 (ASCII for lowercase 'z')

print(ord("0"))  # Returns 48 (ASCII for digit character '0')
print(ord("9"))  # Returns 57 (ASCII for digit character '9')

print(ord(" "))  # Returns 32 (ASCII for space character)

# ------------------------------------------------------------------------------
# 2. chr() Function (Unicode / ASCII Code Point to Character)
# • What is it for:
#   To convert an integer Unicode/ASCII number back into its corresponding character.
# • What it does:
#   Takes an integer code point and returns a single-character string:
#   - chr(88) -> 'X'
#   - chr(45) -> '-' (hyphen / minus)
#   - chr(1), chr(5), chr(22) -> Non-printable ASCII control characters (SOH, ENQ, SYN)
# • Where it is used:
#   Generating alphabet lists without typing them (e.g. [chr(i) for i in range(65, 91)]),
#   decoding raw byte network packets, decrypting encoded secret messages.
# ------------------------------------------------------------------------------
print(chr(88))  # Returns 'X' (ASCII code 88)
print(chr(1))   # Returns SOH (Start of Heading, control character)
print(chr(5))   # Returns ENQ (Enquiry, control character)
print(chr(45))  # Returns '-' (Hyphen/dash)
print(chr(22))  # Returns SYN (Synchronous Idle, control character)
