# ==============================================================================
# Module: Bitwise_operator2.py
# Topic: Advanced Bitwise Operations (NOT ~, Left Shift <<, Right Shift >>)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Bitwise NOT Operator (~) - One's Complement
# • What is it for:
#   Inverts every individual bit of an integer (turning 1 into 0, and 0 into 1).
# • What it does:
#   Python represents signed integers using Two's Complement.
#   The universal formula is: ~n = -(n + 1)
#   For a = 12:
#     ~12 = -(12 + 1) = -13
#   Notice that '~a' evaluates the complement without modifying 'a' itself.
# • Where it is used:
#   Low-level masking, creating inverse masks, negative index indexing from end
#   in C-style arrays (~i pattern), systems programming.
# ------------------------------------------------------------------------------
a = 12
print(~a)       # Result: -13 (inverts all bits, equivalent to -(12 + 1))

# The original variable remains unaffected
print(a)        # Result: 12

# Verification using the underlying Two's Complement formula: b = -(a + 1)
b = -(a + 1)
print(b)        # Result: -13

print("-------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Bitwise Left Shift Operator (<<)
# • What is it for:
#   Shifts all binary bits of the number to the LEFT by specified positions,
#   filling vacant positions on the right with zeros.
# • What it does:
#   Shifting left by 'n' bits mathematically multiplies the number by 2^n:
#   Formula: result = variable * (2 ** number_of_positions)
#   For c = 12 shifted left by 2:
#     12 * (2 ** 2) = 12 * 4 = 48
#   Binary: 0b1100 << 2 = 0b110000 (which is 48)
# • Where it is used:
#   Extremely high-speed multiplication by powers of 2 in performance-critical code,
#   packing multiple data fields into a single integer, graphic color encoding (RGB).
# ------------------------------------------------------------------------------
# Left shift operator
c = 12
print(c << 2)   # Result: 48

# Formula explanation:
# variable * (2 ** number_of_positions)
# 12 * (2 ** 2) = 12 * 4 = 48


# ------------------------------------------------------------------------------
# 3. Bitwise Right Shift Operator (>>)
# • What is it for:
#   Shifts all binary bits of the number to the RIGHT by specified positions,
#   discarding bits that shift off the end.
# • What it does:
#   Shifting right by 'n' bits mathematically performs floor division by 2^n:
#   Formula: result = variable // (2 ** number_of_positions)
#   For c = 12 shifted right by 2:
#     12 // (2 ** 2) = 12 // 4 = 3
#   Binary: 0b1100 >> 2 = 0b0011 (which is 3)
# • Where it is used:
#   Extremely high-speed floor division by powers of 2, binary search mid-point
#   calculation, extracting packed fields (e.g. unpacking RGB color channels).
# ------------------------------------------------------------------------------
# Right shift operator
print(c >> 2)   # Result: 3

# Formula explanation:
# variable // (2 ** number_of_positions)
# 12 // (2 ** 2) = 12 // 4 = 3
