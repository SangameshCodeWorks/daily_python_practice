# ==============================================================================
# Module: implicit_typecasting.py
# Topic: Implicit Type Conversion (Automatic Type Promotion / Coercion)
# ==============================================================================

# In Python, when performing arithmetic between mixed types, Python automatically
# promotes the smaller/narrower data type to the wider data type to prevent data loss.
# Promotion hierarchy: bool -> int -> float -> complex

b = True       # Boolean (promoted to 1 or 1.0 or 1+0j)
i = 5          # Integer
f = 2.1        # Float
c = 3 + 4j     # Complex number

# ------------------------------------------------------------------------------
# 1. bool + int -> int
# • What is it for: Automatically adding boolean flags to counters.
# • What it does: True promotes to 1; 1 + 5 = 6, yielding <class 'int'>.
# • Where it is used: Accumulating count of successful events: total_success += is_valid.
# ------------------------------------------------------------------------------
b_i = b + i
print(b_i)
print(type(b_i))

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 2. bool + float -> float
# • What is it for: Adding boolean flags to decimal balances.
# • What it does: True promotes to 1.0; 1.0 + 2.1 = 3.1, yielding <class 'float'>.
# • Where it is used: Adding a 1.0 flat fee or surcharge flag to a decimal transaction.
# ------------------------------------------------------------------------------
b_f = b + f
print(b_f)
print(type(b_f))

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 3. bool + complex -> complex
# • What is it for: Adding boolean states into complex arithmetic.
# • What it does: True promotes to (1+0j); (1+0j) + (3+4j) = (4+4j), yielding <class 'complex'>.
# • Where it is used: Signal modulation algorithms where boolean bits modulate a complex carrier wave.
# ------------------------------------------------------------------------------
b_c = b + c
print(b_c)
print(type(b_c))

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 4. int + float -> float
# • What is it for: Combining discrete quantities with fractional quantities.
# • What it does: Integer 5 is promoted to float 5.0; 5.0 + 2.1 = 7.1, yielding <class 'float'>.
# • Where it is used: Calculating total bill when multiplying integer item quantities by float unit prices.
# ------------------------------------------------------------------------------
i_f = i + f
print(i_f)
print(type(i_f))

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 5. int + complex -> complex
# • What is it for: Shifting complex numbers along the real axis using an integer.
# • What it does: 5 promotes to (5+0j); (5+0j) + (3+4j) = (8+4j), yielding <class 'complex'>.
# • Where it is used: Adding DC offset voltages to AC electrical signals.
# ------------------------------------------------------------------------------
i_c = i + c
print(i_c)
print(type(i_c))

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 6. float + complex -> complex
# • What is it for: Combining floating-point scalars with complex numbers.
# • What it does: 2.1 promotes to (2.1+0j); (2.1+0j) + (3+4j) = (5.1+4j), yielding <class 'complex'>.
# • Where it is used: Scientific calculations, physics modeling (e.g. quantum wave functions, impedance).
# ------------------------------------------------------------------------------
f_c = f + c
print(f_c)
print(type(f + c))

print("----------------------------------------")
