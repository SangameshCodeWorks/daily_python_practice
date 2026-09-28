# ==============================================================================
# Module: explicit_typecasting.py
# Topic: Explicit Type Casting / Conversion (int, float, complex, bool)
# ==============================================================================

# Base variables of fundamental data types
b = True       # Boolean
i = 5          # Integer
f = 2.1        # Float
c = 3 + 4j     # Complex number

# ------------------------------------------------------------------------------
# 1. Converting Boolean to Integer: int(b)
# • What is it for: Representing boolean true/false as a numeric binary flag.
# • What it does: Converts True to 1 (False would convert to 0) -> prints 1.
# • Where it is used: Summing boolean condition checks (e.g. counting how many passed tests: sum([True, False, True])).
# ------------------------------------------------------------------------------
i_b = int(b)
print(i_b)

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 2. Converting Boolean to Float: float(b)
# • What is it for: Using boolean flags in continuous floating-point equations.
# • What it does: Converts True to 1.0 (False becomes 0.0) -> prints 1.0.
# • Where it is used: Weights and probability calculations in statistical algorithms.
# ------------------------------------------------------------------------------
f_b = float(b)
print(f_b)

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 3. Converting Boolean to Complex: complex(b)
# • What is it for: Embedding boolean states into complex-number planes.
# • What it does: Converts True into (1+0j) with real part 1 and imaginary part 0.
# • Where it is used: Digital signal processing and alternating current (AC) circuit analysis simulations.
# ------------------------------------------------------------------------------
c_b = complex(b)
print(c_b)

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 4. Converting Integer to Float: float(i)
# • What is it for: Promoting whole numbers to decimal precision for accurate division.
# • What it does: Converts 5 to 5.0 -> prints 5.0.
# • Where it is used: Financial math to avoid integer truncation issues, plotting graph coordinates.
# ------------------------------------------------------------------------------
i_f = float(i)
print(i_f)

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 5. Converting Integer to Complex: complex(i)
# • What is it for: Creating a complex number from a real integer.
# • What it does: Converts integer 5 to (5+0j) -> prints (5+0j).
# • Where it is used: Quantum computing simulations, impedance calculations in electronics.
# ------------------------------------------------------------------------------
i_c = complex(i)
print(i_c)

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 6. Converting Float to Complex: complex(f)
# • What is it for: Promoting floating point numbers into complex representations.
# • What it does: Converts float 2.1 to (2.1+0j) -> prints (2.1+0j).
# • Where it is used: Fourier transforms, mathematical waveform computations.
# ------------------------------------------------------------------------------
c_f = complex(f)
print(c_f)

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 7. Truthiness Evaluation: bool() on Numbers
# • What is it for: Checking whether a numeric value is truthy (non-zero) or falsy (zero).
# • What it does:
#   - bool(5): Non-zero integer -> True.
#   - bool(2.1): Non-zero float -> True.
#   - bool(3+4j): Non-zero complex -> True.
#   (Only 0, 0.0, and 0j evaluate to False).
# • Where it is used: Conditional statements like if count: do_something() to test for presence of data.
# ------------------------------------------------------------------------------
bi = bool(i)
print(bi)

print("----------------------------------------")

bf = bool(f)
print(bf)

print("----------------------------------------")

bc = bool(c)
print(bc)

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 8. Converting Float to Integer: int(f) (Truncation)
# • What is it for: Discarding decimal fractions to get whole numbers.
# • What it does: Truncates 2.1 down to 2 (note: does not round, simply chops decimals) -> prints 2.
# • Where it is used: Pixel screen coordinates, indexing arrays, calculating whole items that fit in a box.
# ------------------------------------------------------------------------------
iff = int(f)
print(iff)

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 9. Invalid Conversions: complex to int / float
# • What is it for: Understanding Python type conversion limitations.
# • What it does:
#   Attempting int(c) or float(c) raises:
#   TypeError: can't convert complex to int / float.
#   Because a complex number has both a real and imaginary part, Python cannot determine
#   which scalar value to keep without explicit instruction (e.g. c.real or c.imag).
# • Where it is used: Important interview concept and common debugging gotcha.
# ------------------------------------------------------------------------------
# ic = int(c)
# print(ic)

print("----------------------------------------")

#fc = float(c)
#print(fc)

print("----------------------------------------")
