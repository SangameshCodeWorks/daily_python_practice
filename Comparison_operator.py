# ==============================================================================
# Module: Comparison_operator.py
# Topic: Relational / Comparison Operators (==, !=, >, <, >=, <=)
# ==============================================================================

# Define operands to compare
a = 27
b = 7

# ------------------------------------------------------------------------------
# 1. Equal To (==)
# • What is it for: Checking whether two values are strictly equal.
# • What it does: Compares 27 and 7; since they are not equal, returns False.
# • Where it is used: Validating passwords, checking if user input matches expected command, matching IDs.
# ------------------------------------------------------------------------------
print(a == b)

# ------------------------------------------------------------------------------
# 2. Not Equal To (!=)
# • What is it for: Checking whether two values are different from each other.
# • What it does: Compares 27 and 7; since they are different, returns True.
# • Where it is used: Ensuring a required field is not empty (field != ""), error checking, preventing duplicate entries.
# ------------------------------------------------------------------------------
print(a != b)

# ------------------------------------------------------------------------------
# 3. Greater Than (>)
# • What is it for: Checking if the left value is strictly larger than the right value.
# • What it does: Evaluates 27 > 7 -> True.
# • Where it is used: Age verification (age > 18), checking if stock balance exceeds minimum threshold.
# ------------------------------------------------------------------------------
print(a > b)

# ------------------------------------------------------------------------------
# 4. Less Than (<)
# • What is it for: Checking if the left value is strictly smaller than the right value.
# • What it does: Evaluates 27 < 7 -> False.
# • Where it is used: Checking if battery is below 20%, verifying budget limits, loop boundary conditions.
# ------------------------------------------------------------------------------
print(a < b)

# ------------------------------------------------------------------------------
# 5. Greater Than or Equal To (>=)
# • What is it for: Checking if the left value is either larger than or equal to the right value.
# • What it does: Evaluates 27 >= 7 -> True.
# • Where it is used: Passing grade criteria (marks >= 40), eligibility requirements (credit_score >= 700).
# ------------------------------------------------------------------------------
print(a >= b)

# ------------------------------------------------------------------------------
# 6. Less Than or Equal To (<=)
# • What is it for: Checking if the left value is either smaller than or equal to the right value.
# • What it does: Evaluates 27 <= 7 -> False.
# • Where it is used: Rate limiting (requests <= 100 per minute), discount thresholds (price <= max_budget).
# ------------------------------------------------------------------------------
print(a <= b)
