# ==============================================================================
# Module: Logical_operators.py
# Topic: Boolean Logic and Truth Tables (and, or)
# ==============================================================================

#Logical operators

# ------------------------------------------------------------------------------
# 1. Logical AND Operator (Conjunction)
# • What is it for:
#   Combining multiple conditions where ALL conditions must be True.
# • What it does:
#   - True and True   -> True  (Both sides true)
#   - True and False  -> False (One side is false)
#   - False and True  -> False (Short-circuits immediately at first False)
#   - False and False -> False (Both false)
# • Where it is used:
#   Login authentication (username_valid and password_correct),
#   checking ranges (age >= 18 and age <= 65), verifying permissions and active session.
# ------------------------------------------------------------------------------
print(True and True)    # Result: True
print(True and False)   # Result: False
print(False and True)   # Result: False
print(False and False)  # Result: False

print("..................................................")

# ------------------------------------------------------------------------------
# 2. Logical OR Operator (Disjunction)
# • What is it for:
#   Combining multiple conditions where AT LEAST ONE condition must be True.
# • What it does:
#   - True or True   -> True  (Short-circuits immediately at first True)
#   - True or False  -> True  (First condition is true)
#   - False or True  -> True  (Second condition is true)
#   - False or False -> False (Neither condition is true)
# • Where it is used:
#   Allowing alternative inputs (login with email or phone number),
#   checking discount qualifications (is_student or is_senior_citizen),
#   fallback defaults.
# ------------------------------------------------------------------------------
print(True or True)     # Result: True
print(True or False)    # Result: True
print(False or True)    # Result: True
print(False or False)   # Result: False

print("..................................................")
