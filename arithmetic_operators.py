# ==============================================================================
# Module: arithmetic_operators.py
# Topic: Arithmetic Operators in Python (+, -, *, /, %, //, **)
# ==============================================================================

# Initialize test operand variables
a = 10
b = 4

# ------------------------------------------------------------------------------
# 1. Addition (+)
# • What is it for: Adding two numeric values together.
# • What it does: Computes the mathematical sum of 10 and 4 -> 14.
# • Where it is used: Calculating shopping cart totals, incrementing counters, financial balances.
# ------------------------------------------------------------------------------
print(a + b)

# ------------------------------------------------------------------------------
# 2. Subtraction (-)
# • What is it for: Subtracting the right operand from the left operand.
# • What it does: Computes the difference between 10 and 4 -> 6.
# • Where it is used: Calculating discounts, computing remaining stock/inventory, time differences.
# ------------------------------------------------------------------------------
print(a - b)

# ------------------------------------------------------------------------------
# 3. Multiplication (*)
# • What is it for: Multiplying two numbers.
# • What it does: Computes the product of 10 and 4 -> 40.
# • Where it is used: Calculating area/dimensions, scaling values, pricing items by quantity.
# ------------------------------------------------------------------------------
print(a * b)

# ------------------------------------------------------------------------------
# 4. Standard Float Division (/)
# • What is it for: Performing true mathematical division.
# • What it does: Divides 10 by 4 and returns a floating-point quotient -> 2.5.
# • Where it is used: Calculating averages, split bills, converting units (minutes to hours).
# ------------------------------------------------------------------------------
print("quetiont float value", a / b)

# ------------------------------------------------------------------------------
# 5. Modulus Operator (%)
# • What is it for: Finding the remainder after dividing one integer by another.
# • What it does: 10 divided by 4 leaves a remainder of 2 (10 = 4 * 2 + 2) -> 2.
# • Where it is used: Checking even/odd numbers (n % 2 == 0), circular queue indexes, clock time wrapping (minutes % 60).
# ------------------------------------------------------------------------------
print("quetiont float value", a % b)

# ------------------------------------------------------------------------------
# 6. Floor / Integer Division (//)
# • What is it for: Dividing numbers and rounding down to the nearest integer.
# • What it does: Divides 10 by 4 = 2.5 and chops off the fractional part -> 2.
# • Where it is used: Pagination (calculating total number of pages), dividing items evenly among groups.
# ------------------------------------------------------------------------------
print("reminder  value", a // b)

# ------------------------------------------------------------------------------
# 7. Exponentiation / Power (**)
# • What is it for: Raising a base number to the power of an exponent.
# • What it does: Calculates 10 raised to the power of 4 (10^4 = 10 * 10 * 10 * 10) -> 10000.
# • Where it is used: Scientific formulas, compound interest calculations, physics simulations, cryptography.
# ------------------------------------------------------------------------------
print(a ** b)

print(".................................................")
