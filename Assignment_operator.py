# ==============================================================================
# Module: Assignment_operator.py
# Topic: Compound Assignment Operators (+=, -=, *=, /=, //=, %=)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Addition Assignment (+=)
# • What is it for: Adding a value to a variable and updating the variable in-place (a = a + 2).
# • What it does: Starts with a = 8, adds 2 to it, making 'a' equal to 10.
# • Where it is used: Accumulator counters in loops, adding points to a player's score, tracking running totals.
# ------------------------------------------------------------------------------
a = 8
a += 2
print(a)

# ------------------------------------------------------------------------------
# 2. Subtraction Assignment (-=)
# • What is it for: Subtracting a value from a variable in-place (b = b - 2).
# • What it does: Starts with b = 10, subtracts 2, making 'b' equal to 8.
# • Where it is used: Countdown timers, decrementing inventory after a sale, reducing player health points.
# ------------------------------------------------------------------------------
b = 10
b -= 2
print(b)

# ------------------------------------------------------------------------------
# 3. Multiplication Assignment (*=)
# • What is it for: Multiplying variable by a value and assigning the result back (c = c * 2).
# • What it does: Starts with c = 5, multiplies by 2, making 'c' equal to 10.
# • Where it is used: Scaling graphics, doubling values in exponential backoff algorithms, financial growth modeling.
# ------------------------------------------------------------------------------
c = 5
c *= 2
print(c)

# ------------------------------------------------------------------------------
# 4. Division Assignment (/=)
# • What is it for: Dividing variable by a value and storing the floating-point result.
# • What it does: Divides variable 'a' (currently 10) by 2 resulting in 5.0.
#   Note: Variable 'd' remains 10 because 'd' was not modified.
# • Where it is used: Halving search intervals (binary search), normalization of features in machine learning.
# ------------------------------------------------------------------------------
d = 10
a /= 2
print(d)

# ------------------------------------------------------------------------------
# 5. Floor Division Assignment (//=)
# • What is it for: Dividing variable and truncating decimal part in-place (e = e // 2).
# • What it does: Starts with e = 7, divides by 2 to get 3.5, floors to 3.
# • Where it is used: Repeatedly dividing digits in number manipulation (e.g. reversing a number or base conversion).
# ------------------------------------------------------------------------------
e = 7
e //= 2
print(e)

# ------------------------------------------------------------------------------
# 6. Modulo Assignment (%=)
# • What is it for: Updating variable with the remainder of division (f = f % 2).
# • What it does: Starts with f = 8, divides by 2, remainder is 0, so 'f' becomes 0.
# • Where it is used: Constraining an incrementing index within a fixed range (wrap-around ring buffers).
# ------------------------------------------------------------------------------
f = 8
f %= 2
print(f)

# ------------------------------------------------------------------------------
# 7. Another Multiplication Assignment (*=)
# • What is it for: Scaling variable 'g' by a multiplier.
# • What it does: Starts with g = 4, multiplies by 2 -> 8.
# • Where it is used: Speed multipliers, zooming scale factors in UI applications.
# ------------------------------------------------------------------------------
g = 4
g *= 2
print(g)
