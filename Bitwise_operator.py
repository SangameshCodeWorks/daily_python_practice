# ==============================================================================
# Module: Bitwise_operator.py
# Topic: Bitwise Binary Operators (AND &, OR |, XOR ^)
# ==============================================================================

# Operands for bitwise evaluation
# 12 in binary: 0b1100
#  5 in binary: 0b0101

# ------------------------------------------------------------------------------
# 1. Bitwise AND Operator (&)
# • What is it for:
#   Compares two numbers at their binary bit level. For each bit position,
#   it outputs 1 if and only if BOTH corresponding bits are 1.
# • What it does:
#   12 = 1100 (in binary)
#    5 = 0101 (in binary)
#   ---------------
#   &  = 0100 -> Decimal 4
# • Where it is used:
#   Bitmasking, checking if a specific bit/flag is active (e.g., file permissions),
#   clearing bits, IP address network masking (subnet masks), low-level device drivers.
# ------------------------------------------------------------------------------
# Bitwise AND operator
# Converts operands into binary and compares them bit-by-bit using AND logic
print(12 & 5)   # Result: 4 (0b0100)

print("-------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Bitwise OR Operator (|)
# • What is it for:
#   Compares two numbers at their binary bit level. For each bit position,
#   it outputs 1 if AT LEAST ONE of the corresponding bits is 1.
# • What it does:
#   12 = 1100 (in binary)
#    5 = 0101 (in binary)
#   ---------------
#   |  = 1101 -> Decimal 13 (8 + 4 + 1)
# • Where it is used:
#   Combining multiple status or configuration flags together, turning on
#   specific bits without altering other bits, graphics processing.
# ------------------------------------------------------------------------------
# Bitwise OR operator
print(12 | 5)   # Result: 13 (0b1101)

print("-------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Bitwise XOR Operator (^)
# • What is it for:
#   Exclusive OR: outputs 1 only when corresponding bits are DIFFERENT (one is 1, one is 0).
#   If both bits are identical (both 1 or both 0), it yields 0.
# • What it does:
#   12 = 1100 (in binary)
#    5 = 0101 (in binary)
#   ---------------
#   ^  = 1001 -> Decimal 9 (8 + 1)
# • Where it is used:
#   Toggling flags (flipping bits), basic cryptography/ciphers, checksum algorithms,
#   swapping two variables without a temporary variable, parity checks.
# ------------------------------------------------------------------------------
# Bitwise XOR operator
print(12 ^ 5)   # Result: 9 (0b1001)
